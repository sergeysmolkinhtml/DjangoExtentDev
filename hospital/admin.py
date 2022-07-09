from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from hospital.models import *
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver



@receiver(setting_changed)
def user_model_swapped(**kwargs):
    if kwargs['setting'] == 'AUTH_USER_MODEL':
        apps.clear_cache()
        from myapp import some_module
        some_module.UserModel = get_user_model()


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','patronymic','years',)
    list_display_links = ('id','first_name','last_name',)
admin.site.register(Doctor,DoctorAdmin)


class DoctorSpecialityAdmin(admin.ModelAdmin):
    pass
admin.site.register(DoctorSpeciality,DoctorSpecialityAdmin)

class WorkingTimesAdmin(admin.ModelAdmin):
    pass
admin.site.register(WorkingTimes,WorkingTimesAdmin)

class PolyclynicAdmin(admin.ModelAdmin):
    pass
admin.site.register(Polyclinyc,PolyclynicAdmin)


admin.site.register(Priyom)
admin.site.register(ClinicType)
admin.site.register(HelsiReviews)
admin.site.register(ConsultationSchedule)
admin.site.register(Gender)
admin.site.register(Cabinet)
admin.site.register(DoctorRating)


class ProfileAdmin(admin.ModelAdmin):
   list_display = ('id','user',)
   fields = ('user',)

admin.site.register(Profile, ProfileAdmin)