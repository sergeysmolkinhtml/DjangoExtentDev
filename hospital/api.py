from rest_framework import generics
from hospital.models import Doctor
from .serializers import DoctorSerializer
from rest_framework.views import APIView
import json
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins

