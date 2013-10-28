from manager.models import *
from manager.forms import *
import Image
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def background(request,seccion):
  # Secciones
  try:
    sec = Background.objects.get(seccion=seccion)
  except:
    sec = None
  if request.method == 'POST':
    formulario = BackgroundForm(request.POST,request.FILES)
    if formulario.is_valid():
      imagen = formulario.cleaned_data['imagen']
      alineacion1 = formulario.cleaned_data['alineacion1']
      alineacion2 = formulario.cleaned_data['alineacion2']
      size1 = formulario.cleaned_data['size1']
      size2 = formulario.cleaned_data['size2']
      if sec == None:
        sec = Background.objects.create(seccion=seccion,imagen=imagen,alineacion1=alineacion1,alineacion2=alineacion2,size1=size1,size2=size2)
        sec.save()
      else:
        if request.POST.get('imagen-clear') == 'on':
          imagen = None
          sec.imagen = None
        if imagen != None:
          sec.imagen = imagen
        sec.alineacion1 = alineacion1
        sec.alineacion2 = alineacion2
        sec.size1 = size1
        sec.size2 = size2
        sec.save()
  if sec != None:
    formulario = BackgroundForm(initial={'imagen':sec.imagen,'alineacion1':sec.alineacion1,'alineacion2':sec.alineacion2,'size1':sec.size1,'size2':sec.size2})
  else:
    formulario = BackgroundForm()
  return render_to_response('background.html',{'formulario':formulario}, context_instance=RequestContext(request))

def planos(request,edif):
  # Secciones
  try:
    edificio = Planos.objects.get(edificio=edif)
  except:
    edificio = None
  if request.method == 'POST':
    formulario = PlanosForm(request.POST,request.FILES)
    if formulario.is_valid():
      imagen = formulario.cleaned_data['imagen']
      alineacion1 = formulario.cleaned_data['alineacion1']
      alineacion2 = formulario.cleaned_data['alineacion2']
      size1 = formulario.cleaned_data['size1']
      size2 = formulario.cleaned_data['size2']
      if edificio == None:
        edificio = Planos.objects.create(edificio=edif,imagen=imagen,alineacion1=alineacion1,alineacion2=alineacion2,size1=size1,size2=size2)
        edificio.save()
      else:
        if request.POST.get('imagen-clear') == 'on':
          imagen = None
          edificio.imagen = None
        if imagen != None:
          edificio.imagen = imagen
        edificio.alineacion1 = alineacion1
        edificio.alineacion2 = alineacion2
        edificio.size1 = size1
        edificio.size2 = size2
        edificio.save()
  if edificio != None:
    formulario = PlanosForm(initial={'imagen':edificio.imagen,'alineacion1':edificio.alineacion1,'alineacion2':edificio.alineacion2,'size1':edificio.size1,'size2':edificio.size2})
  else:
    formulario = PlanosForm()
  return render_to_response('planos.html',{'formulario':formulario}, context_instance=RequestContext(request))

def galeriasImagenes(request,gale):
  # Secciones
  try:
    galeria = GaleriasImagenes.objects.get(nombreGaleria=gale)
  except:
    galeria = None
  if request.method == 'POST':
    formulario = GaleriasImagenesForm(request.POST,request.FILES)
    if formulario.is_valid():
      imagen = formulario.cleaned_data['imagenes']
      alineacion1 = formulario.cleaned_data['alineacion1']
      alineacion2 = formulario.cleaned_data['alineacion2']
      size1 = formulario.cleaned_data['size1']
      size2 = formulario.cleaned_data['size2']
      if galeria == None:
        galeria = GaleriasImagenes.objects.create(nombreGaleria=gale)
        imagenes = Imagenes.objects.create(imagen=imagen,alineacion1=alineacion1,alineacion2=alineacion2,size1=size1,size2=size2)
        galeria.save()
        imagenes.save()
        #Agregando ManyToMany
        galeria.imagenes.add(imagenes)
        galeria.save()
      else:
        imagenes = Imagenes.objects.create(imagen=imagen,alineacion1=alineacion1,alineacion2=alineacion2,size1=size1,size2=size2)
        imagenes.save()
        #Agregando ManyToMany
        galeria.imagenes.add(imagenes)
        galeria.save()

  formulario = GaleriasImagenesForm()
  return render_to_response('galeriasImagenes.html',{'formulario':formulario,'galeria':galeria}, context_instance=RequestContext(request))

def carga_pdf(request,pdf):
  # Secciones
  try:
    galeria_pdf = GaleriasPdf.objects.get(nombreGaleria=pdf)
  except:
    galeria_pdf = None
  if request.method == 'POST':
    formulario = PdfForm(request.POST,request.FILES)
    if formulario.is_valid():
      archivo_pdf = formulario.cleaned_data['pdf']
      if galeria_pdf == None:
        galeria_pdf = GaleriasPdf.objects.create(nombreGaleria=pdf)
        galeria_pdf.save()

      else:
        for galeria in galeria_pdf.pdf.all():
          galeria.delete()

      pdf_creado = Pdf.objects.create(pdf=archivo_pdf)
      galeria_pdf.pdf.add(pdf_creado)
      pdf_creado.save()
      galeria_pdf.save()

  if galeria_pdf != None:
    for galeria in galeria_pdf.pdf.all():
      gale_pdf = galeria
      print gale_pdf
    formulario = PdfForm(initial={'pdf':gale_pdf.pdf})
  else:
    formulario = PdfForm()

  return render_to_response('carga_pdf.html',{'formulario':formulario}, context_instance=RequestContext(request))
