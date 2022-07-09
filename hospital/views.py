from django_filters.rest_framework import DjangoFilterBackend
import requests
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView,MultipleObjectMixin,BaseListView
from .models import *
from  django.views.generic.base import TemplateView
from rest_framework.response import Response
from django.views.generic import DetailView,View,CreateView,ListView
from django.views.generic.edit import CreateView,FormMixin,ProcessFormView,FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .utils import *
from django.views.generic.base import TemplateResponseMixin,ContextMixin
from django.views import generic
from django.shortcuts import render,redirect
from .forms import PriyomForm
from django.db.models import Q
from django.core.paginator import Paginator
class index(generic.ListView):
    template_name = 'hospital/index.html'
    context_object_name = 'specia'

    def get_context_data(self):
        context = super(index, self).get_context_data()
        context['reviews'] = HelsiReviews.objects.values('comment')
        context['docnames'] = Doctor.objects.filter(years__lt=66).\
            select_related('rating','cabinet').\
                only('rating__star','cabinet__cabinet_number',).\
                values('rating','rating__star', 'cabinet','cabinet__cabinet_number','years','first_name')
        return context

    def get_queryset(self):
        return DoctorSpeciality.objects.values('title')[:5]

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)


class Profile(DetailView):
    model = Profile
    template_name = 'hospital/profile-detail.html'

class YearGenderExperience:

    def get_years(self):
        return Doctor.objects.values_list('years')

    def get_gender(self):
        return Gender.objects.all()


class OnlineCons(YearGenderExperience,FormView,ContextMixin,generic.View):
    template_name = 'hospital/online-cons.html'
    form_class = PriyomForm

    def get(self,request):
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self,request):
        if request.method == 'POST':
            pacient = Priyom.objects.get(pacient_id=self.pacient_id)
            form = PriyomForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()
                return redirect('/')
            else:
                form = PriyomForm()
        return render(request,'hospital/online-cons.html',context={'form':form})

    def get_context_data(self, **kwargs):
        context = super(OnlineCons, self).get_context_data()
        context['doctors'] = Doctor.objects.all().select_related('specitality','polyclynic','polyclynic__type')\
        .prefetch_related('polyclynic__type').defer('rating','gender','profile','working_times','online_consultation','conditions_to_appmt','cabinet','accepts_declarations',)
        context['schedule'] = ConsultationSchedule.objects.select_related('doctor')\
        .defer('doctor__first_name','doctor__last_name','doctor__patronymic','doctor__gender','doctor__photo','doctor__working_times','doctor__online_consultation','doctor__specitality','doctor__experience','doctor__conditions_to_appmt','doctor__cabinet','doctor__accepts_declarations',
        'doctor__polyclynic','doctor__profile','doctor__rating','doctor__years')\
        .filter(active=False).order_by('date')
        #context['priyom'] = Priyom.objects.all()
        #context['form'] = PriyomForm
        return context

class FilterDoctorsView(YearGenderExperience,ListView):
    def get_queryset(self):
        if self.request.GET.getlist("gender") and self.request.GET.getlist("years"):
            queryset = Doctor.objects.filter(years__in=self.request.GET.getlist("years"),
                                            gender__in=self.request.GET.getlist("gender"))
        else:
            queryset = Doctor.objects.filter(
                Q(years__in=self.request.GET.getlist("years")) | Q(gender__in=self.request.GET.getlist("gender")))
        return queryset

    template_name = 'hospital/online-cons.html'
class ClinicView(ListView):
    template_name = 'hospital/polyclynic.html'
    queryset = Polyclinyc.objects.all()











