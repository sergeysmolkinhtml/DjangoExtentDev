import datetime

from django.db import models
import time
from time import timezone
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.signals import request_started
class Doctor(models.Model):
    first_name = models.CharField(max_length=130,null=True)
    last_name = models.CharField(max_length=100,null=True)
    patronymic = models.CharField(max_length=100,null=True)
    gender = models.ForeignKey('Gender',on_delete=models.DO_NOTHING,default='')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',null=True)
    years = models.IntegerField()
    working_times = models.ForeignKey('WorkingTimes',on_delete=models.CASCADE,null=True,verbose_name='График')
    online_consultation = models.BooleanField(default=True)
    specitality = models.ForeignKey('DoctorSpeciality',on_delete=models.SET_DEFAULT,default='')
    experience = models.SmallIntegerField(default='1')
    conditions_to_appmt = models.TextField(max_length=1000,default='Бесплатно')
    cabinet = models.ForeignKey('Cabinet',on_delete=models.DO_NOTHING,default='')
    accepts_declarations = models.BooleanField(default=True)
    polyclynic = models.ForeignKey('Polyclinyc',on_delete=models.CASCADE,related_name='doctors work place+',default='',null=True,blank=True)
    consultation_schedule = models.ManyToManyField('ConsultationSchedule',related_name='consultai_schedule+',blank=True)
    rating = models.ForeignKey('DoctorRating',on_delete=models.CASCADE,null=True)
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | возраст - {self.years} | клиника {self.polyclynic}'

    class Meta:
        default_related_name = 'all_doctors'
        ordering = ['-years']

choicewhogo = [
    ('ALONE','записати себе'),
    ("MY_CHILD","записати дитину")
]
choiceConsType = [
    ('ONLINE',"видеоконсльтация"),
    ("MYSELF","прийду до ликаря")
]

class Priyom(models.Model):
    pacient = models.ForeignKey('Profile',on_delete=models.DO_NOTHING,null=True,blank=True)
    doctor = models.ForeignKey('Doctor',on_delete=models.DO_NOTHING,null=True,blank=True)
    date = models.ForeignKey('ConsultationSchedule',on_delete=models.DO_NOTHING,null=True)
    active = models.BooleanField(default=False,blank=True)
    consType = models.CharField(max_length=100,choices=choiceConsType,null=True)
    choicewhogo = models.CharField(max_length=100,choices=choicewhogo,null=True)

   #const id=self.dateid active true ПО ФАКТУ МНЕ НАДО ПЕРЕДАТЬ ДАННЫЕ С КОНСУЛЬ СКЕДУЛА НА ПРИЙОМ
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        ConsultationSchedule.objects.filter(id=self.date.id).update(active=True)
        return super(Priyom, self).save()

    def __str__(self):
        return f'active - {self.active} | {self.date} -|- пациэнт - {self.pacient} | доктор - {self.doctor.first_name}  {self.doctor.last_name}'

class ConsultationSchedule(models.Model):
    date = models.DateTimeField(u'Дата и время', default=timezone.now)
    doctor = models.ForeignKey('Doctor',null=True,on_delete=models.DO_NOTHING,related_name='doctor schedule con+')
    active = models.BooleanField(default=False,blank=True) #занято ли место
    profile = models.ForeignKey('Profile',on_delete=models.DO_NOTHING,null=True)

    def save(self, *args, **kwargs):
        dates = ConsultationSchedule.objects.filter(
            date__year=self.date.year,
            date__month=self.date.month,
            date__day=self.date.day,
            date__hour=self.date.hour,
            date__minute=self.date.minute + 100
        )
        if dates.exists() > 0:
            raise ValueError('same date error')
        else:
            super(ConsultationSchedule, self).save(*args, **kwargs)

    def __str__(self):
        return f' занято - {self.active} | к {self.doctor.first_name} {self.doctor.last_name} на {self.date.day}.0{self.date.month}.{self.date.year} в {self.date.hour}:{self.date.minute}'

class Gender(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'

class DoctorRating(models.Model):
    star = models.FloatField()

    def __str__(self):
        return f'{self.star}'

class Cabinet(models.Model):
    cabinet_number = models.IntegerField()

    def __str__(self):
        return f'{self.cabinet_number}'

class DoctorSpeciality(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


PONEDELNIK = 'ПОНЕДЕЛЬНИК'
VTORNIK = 'Вторник'
SREDA = 'Среда'
CHETVERG = 'Четверг'
PYTNISTSA = 'Пятница'
SUBBOTA = 'Суббота'
VOSKRESENYE = 'Воскресенье'


WEEKDAYS = [
    (PONEDELNIK, ("Понедельник")),
    (VTORNIK, ("Вторник")),
    (SREDA, ("Среда")),
    (CHETVERG, ("Четверг")),
    (PYTNISTSA, ("Пятница")),
    (SUBBOTA, ("Суббота")),
    (VOSKRESENYE, ("Воскресенье")),
 ]

class WorkingTimes(models.Model):
    from_weekday = models.CharField(
        choices=WEEKDAYS,
        unique=False,verbose_name='с какого дня',max_length=200)
    to_weekday = models.CharField(
        choices=WEEKDAYS,
        unique=False,
        max_length=100
    )
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    def __str__(self):
        return f'с {self.from_weekday} до {self.to_weekday} | c {self.from_hour} до {self.to_hour}'

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = "Графики"



class Polyclinyc(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    workingtimes= models.ForeignKey('WorkingTimes',on_delete=models.CASCADE,null=True)
    description = models.TextField()
    specialities = models.ManyToManyField('DoctorSpeciality')
    doctor = models.ManyToManyField('Doctor',unique=False,blank=True)
    type = models.ForeignKey('ClinicType',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.title}'

class ClinicType(models.Model):
    title = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.title}"
class HelsiReviews(models.Model):
    comment = models.TextField()

    def __str__(self):
        return f'{self.comment}'

class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name="Пользователь",on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    years = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
       return reverse('profile',kwargs={'id':self.id})




@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()