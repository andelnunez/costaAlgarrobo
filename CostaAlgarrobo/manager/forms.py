#encoding:utf-8
import datetime
from django.forms import ModelForm
from django.db import models
from django import forms
from django.contrib.auth.models import User
from manager.models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.extras.widgets import *

class BackgroundForm(forms.Form):
  aligV = (
    ('top','Arriba'),
    ('middle','Medio'),
    ('bottom','Abajo'),
  )
  aligH = (
    ('left','Izquierda'),
    ('center','Centro'),
    ('right','Derecha'),
  )
  seccion = forms.ModelMultipleChoiceField(queryset=Seccion.objects.all())
  nombre = forms.CharField(max_length=100)
  imagen = forms.ImageField(required=False)
  alineacion1 = forms.ChoiceField(choices=aligV)
  alineacion2 = forms.ChoiceField(choices=aligH)

class PlanosForm(forms.Form):
  imagen = forms.ImageField(required=False)
  alineacion1 = forms.CharField(max_length=20)
  alineacion2 = forms.CharField(max_length=20)
  size1 = forms.CharField(max_length=20)
  size2 = forms.CharField(max_length=20)

class GaleriasImagenesForm(forms.Form):
  aligV = (
    ('Top','Arriba'),
    ('Middle','Medio'),
    ('Bottom','Abajo'),
  )
  aligH = (
    ('Left','Izquierda'),
    ('Center','Centro'),
    ('Right','Derecha'),
  )
  nombre = forms.CharField(max_length=100)
  imagenes = forms.ImageField()
  alineacion1 = forms.ChoiceField(choices=aligV)
  alineacion2 = forms.ChoiceField(choices=aligH)
  size1 = forms.CharField(max_length=20)
  size2 = forms.CharField(max_length=20)

class PdfForm(forms.Form):
  pdf = forms.FileField()

class VideoForm(forms.Form):
  video = forms.FileField()

class TextoForm(ModelForm):
  class Meta:
    model = Texto
    exclude = ['seccion']

class ContactoForm(forms.Form):
  nombre = forms.CharField(min_length=2, max_length=50)
  rut = forms.CharField(min_length=2, max_length=100)
  direccion = forms.CharField(min_length=2, max_length=400)
  telefono = forms.IntegerField()
  celular = forms.IntegerField()
  email = forms.EmailField()
  consulta = forms.Textarea()
