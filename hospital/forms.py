from typing import List, Tuple
import urllib.request
from django import forms
from django.forms import ModelForm
from .models import Priyom,ConsultationSchedule,Doctor


class PriyomForm(forms.ModelForm):

    class Meta:
        model = Priyom
        fields = '__all__'





