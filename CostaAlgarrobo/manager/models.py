#encoding:utf-8
from django.db.models.fields.related import ManyToManyField
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Seccion(models.Model):
  nombre = models.CharField(max_length=100)
  def __unicode__(self):
    return self.nombre
  class Meta:
        verbose_name = "Seccione"

class SubSeccion(models.Model):
  nombre = models.CharField(max_length=100)
  seccion = models.ForeignKey(Seccion)
  def __unicode__(self):
    return self.nombre

class ImagenesTransparente(models.Model):
  def __unicode__(self):
    return self.nombre
  nombre = models.CharField(max_length=100)
  imagen = models.ImageField(upload_to='carga')
  class Meta:
        verbose_name = "Imagenes Transparente"


class Background(models.Model):
  def __unicode__(self):
    return self.nombre
  aligV = (
    ('top','Arriba'),
    ('center','Medio'),
    ('bottom','Abajo'),
  )
  aligH = (
    ('left','Izquierda'),
    ('center','Centro'),
    ('right','Derecha'),
  )
  nombre = models.CharField(max_length=100)
  seccion = models.ManyToManyField(Seccion)
  imagen = models.ImageField(upload_to='carga')
  alto = models.CharField(max_length=20)
  ancho = models.CharField(max_length=20)
  vertical = models.CharField(max_length=20, choices=aligV)
  horizontal = models.CharField(max_length=20, choices=aligH)
  asociada = models.ForeignKey(ImagenesTransparente, null=True)
  class Meta:
        verbose_name = "Fondo"

class Edificio(models.Model):
  def __unicode__(self):
    return self.nombre
  nombre = models.CharField(max_length=100)

class Tipo(models.Model):
  edificio = models.ForeignKey(Edificio)
  nombre = models.CharField(max_length=100)
  def __unicode__(self):
    salida = self.nombre + " - " + self.edificio.nombre
    return salida
  class Meta:
        ordering = ['edificio']

class Planos(models.Model):
  def __unicode__(self):
    return self.edificio

  tipo = models.ForeignKey(Tipo)
  nombre = models.CharField(max_length=100)
  imagen = models.ImageField(upload_to='carga')
  miniplano = models.ImageField(upload_to='carga',verbose_name='Plano Miniatura')
  alto = models.CharField(max_length=20)
  ancho = models.CharField(max_length=20)
  alineacion1 = models.CharField(max_length=20)
  alineacion2 = models.CharField(max_length=20)
  size1 = models.CharField(max_length=20)
  size2 = models.CharField(max_length=20)
  class Meta:
        verbose_name = "Plano"

class GaleriasImagenes(models.Model):
  def __unicode__(self):
    return self.nombreGaleria
  nombreGaleria = models.CharField(max_length=100)
  class Meta:
        verbose_name = "Galerias de Imagene"

class Imagenes(models.Model):
  def __unicode__(self):
    return self.nombre
  nombre = models.CharField(max_length=100)
  imagen = models.ImageField(upload_to='carga')
  alto = models.CharField(max_length=20)
  ancho = models.CharField(max_length=20)
  alineacion1 = models.CharField(max_length=20)
  alineacion2 = models.CharField(max_length=20)
  size1 = models.CharField(max_length=20)
  size2 = models.CharField(max_length=20)
  galeria = models.ForeignKey(GaleriasImagenes)
  class Meta:
        verbose_name = "Imagenes de Galeria"

class Videos(models.Model):
  nombre = models.CharField(max_length=50)
  codigo = models.TextField(max_length=1000)
  class Meta:
        verbose_name = "Video"

class GaleriasVideos(models.Model):
  def __unicode__(self):
    return self.nombreGaleria
  nombreGaleria = models.CharField(max_length=100)
  videos = ManyToManyField(Videos)
  class Meta:
        verbose_name = "Galerias de Video"

class Pdf(models.Model):
  pdf = models.FileField(upload_to='carga')

class GaleriasPdf(models.Model):
  def __unicode__(self):
    return self.nombreGaleria
  nombreGaleria = models.CharField(max_length=100)
  pdf = ManyToManyField(Pdf)
  class Meta:
        verbose_name = "Galerias de Pdf"

class Texto(models.Model):
  seccion = models.ForeignKey(SubSeccion)
  titulo = models.CharField(max_length=100)
  texto = models.TextField(max_length=1000)
  class Meta:
        verbose_name = "Texto"
