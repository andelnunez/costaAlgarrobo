#encoding:utf-8
from django.db.models.fields.related import ManyToManyField
from django.db import models
from django.contrib.auth.models import User

class Background(models.Model):
  def __unicode__(self):
    return self.seccion
  seccion = models.CharField(max_length=100)
  imagen = models.ImageField(upload_to='carga')
  alto = models.CharField(max_length=20)
  ancho = models.CharField(max_length=20)
  alineacion1 = models.CharField(max_length=20)
  alineacion2 = models.CharField(max_length=20)
  size1 = models.CharField(max_length=20)
  size2 = models.CharField(max_length=20)

class Planos(models.Model):
  def __unicode__(self):
    return self.edificio
  edificio = models.CharField(max_length=100)
  imagen = models.ImageField(upload_to='carga')
  alto = models.CharField(max_length=20)
  ancho = models.CharField(max_length=20)
  alineacion1 = models.CharField(max_length=20)
  alineacion2 = models.CharField(max_length=20)
  size1 = models.CharField(max_length=20)
  size2 = models.CharField(max_length=20)

class Imagenes(models.Model):
  imagen = models.ImageField(upload_to='carga')
  alto = models.CharField(max_length=20)
  ancho = models.CharField(max_length=20)
  alineacion1 = models.CharField(max_length=20)
  alineacion2 = models.CharField(max_length=20)
  size1 = models.CharField(max_length=20)
  size2 = models.CharField(max_length=20)

class GaleriasImagenes(models.Model):
  def __unicode__(self):
    return self.nombreGaleria
  nombreGaleria = models.CharField(max_length=100)
  imagenes = ManyToManyField(Imagenes)

class Videos(models.Model):
  video = models.FileField(upload_to='carga')

class GaleriasVideos(models.Model):
  def __unicode__(self):
    return self.nombreGaleria
  nombreGaleria = models.CharField(max_length=100)
  videos = ManyToManyField(Videos)

class Pdf(models.Model):
  pdf = models.FileField(upload_to='carga')

class GaleriasPdf(models.Model):
  def __unicode__(self):
    return self.nombreGaleria
  nombreGaleria = models.CharField(max_length=100)
  pdf = ManyToManyField(Pdf)

