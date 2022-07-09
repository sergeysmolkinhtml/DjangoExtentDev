from django.contrib import admin
from django.urls import path,include,register_converter,re_path
from . import views
from .views import *
from .api import *
from rest_framework.routers import DefaultRouter

class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value): # Метод to_python(self, value), который обрабатывает преобразование согласованной строки в тип
        return int(value)

    def to_url(self, value): # Метод to_url(self, value), который обрабатывает преобразование типа Python в строку
        return '%04d' % value

urlpatterns = [
    path('',index.as_view(),name='index'),
    path('filter/',views.FilterDoctorsView.as_view(),name = 'filterdoc'),
    path('online-cons/', OnlineCons.as_view(), name='cons'),
    path('profile/<int:pk>/',Profile.as_view(),name = 'profile'),
    path('clinics/',ClinicView.as_view(),name = 'clinic'),

]