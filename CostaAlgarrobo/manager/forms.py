#encoding:utf-8
import datetime
from django.forms import ModelForm
from django.db import models
from django import forms
from django.contrib.auth.models import User
from manager.models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.extras.widgets import SelectDateWidget

class BackgroundForm(forms.Form):
  imagen = forms.ImageField(required=False)
  alineacion1 = forms.CharField(max_length=20)
  alineacion2 = forms.CharField(max_length=20)
  size1 = forms.CharField(max_length=20)
  size2 = forms.CharField(max_length=20)

class PlanosForm(forms.Form):
  imagen = forms.ImageField(required=False)
  alineacion1 = forms.CharField(max_length=20)
  alineacion2 = forms.CharField(max_length=20)
  size1 = forms.CharField(max_length=20)
  size2 = forms.CharField(max_length=20)

class GaleriasImagenesForm(forms.Form):
  imagenes = forms.ImageField()
  alineacion1 = forms.CharField(max_length=20)
  alineacion2 = forms.CharField(max_length=20)
  size1 = forms.CharField(max_length=20)
  size2 = forms.CharField(max_length=20)

class PdfForm(forms.Form):
  pdf = forms.FileField()

class VideoForm(forms.Form):
  video = forms.FileField()


