from manager.models import *
from manager.forms import *
import Image
from django.shortcuts import render_to_response
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
import Image
from easy_thumbnails.files import get_thumbnailer
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
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
        sec.ancho = sec.imagen.width 
        sec.alto = sec.imagen.height
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
        if imagen != None:
          sec.ancho = sec.imagen.width 
          sec.alto = sec.imagen.height
          sec.save()
      # Crop
      return HttpResponseRedirect('/crop_background/' + str(sec.id))  
  if sec != None:
    formulario = BackgroundForm(initial={'imagen':sec.imagen,'alineacion1':sec.alineacion1,'alineacion2':sec.alineacion2,'size1':sec.size1,'size2':sec.size2})
  else:
    formulario = BackgroundForm()
  return render_to_response('background.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/')
def crop_background(request,id_back):
  image = Background.objects.get(id=id_back)
  if request.method == "POST":
    im = Image.open(image.imagen)
    box = (int(request.POST.get('x1')),int(request.POST.get('y1')),int(request.POST.get('x2')),int(request.POST.get('y2')))
    cropiado = im.crop(box)
    cropiado.save("CostaAlgarrobo/carga/" + str(image.imagen))
    image.ancho = image.imagen.width
    image.alto = image.imagen.height
    image.save()

    return HttpResponseRedirect('/background/home') 
  return render_to_response('crop.html', {'image': image}, context_instance=RequestContext(request))

@login_required(login_url='/')
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
        edificio.ancho = edificio.imagen.width 
        edificio.alto = edificio.imagen.height
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
        if imagen != None:
          edificio.ancho = edificio.imagen.width 
          edificio.alto = edificio.imagen.height
          edificio.save()
      return HttpResponseRedirect('/crop_planos/' + str(edificio.id))
  if edificio != None:
    formulario = PlanosForm(initial={'imagen':edificio.imagen,'alineacion1':edificio.alineacion1,'alineacion2':edificio.alineacion2,'size1':edificio.size1,'size2':edificio.size2})
  else:
    formulario = PlanosForm()
  return render_to_response('planos.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/')
def crop_planos(request,id_plano):
  image = Planos.objects.get(id=id_plano)
  if request.method == "POST":
    im = Image.open(image.imagen)
    box = (int(request.POST.get('x1')),int(request.POST.get('y1')),int(request.POST.get('x2')),int(request.POST.get('y2')))
    cropiado = im.crop(box)
    cropiado.save("CostaAlgarrobo/carga/" + str(image.imagen))
    image.ancho = image.imagen.width
    image.alto = image.imagen.height
    image.save()
    return HttpResponseRedirect('/planos/' + image.edificio)   
  return render_to_response('crop.html', {'cortar':'planos','image': image}, context_instance=RequestContext(request))

@login_required(login_url='/')
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
        imagenes.ancho = imagenes.imagen.width 
        imagenes.alto = imagenes.imagen.height
        imagenes.save()

        #Agregando ManyToMany
        galeria.imagenes.add(imagenes)
        galeria.save()
      else:
        imagenes = Imagenes.objects.create(imagen=imagen,alineacion1=alineacion1,alineacion2=alineacion2,size1=size1,size2=size2)
        imagenes.save()
        imagenes.ancho = imagenes.imagen.width 
        imagenes.alto = imagenes.imagen.height
        imagenes.save()

        #Agregando ManyToMany
        galeria.imagenes.add(imagenes)
        galeria.save()
      return HttpResponseRedirect('/crop_galeriasImagenes/' + gale + '/' + str(imagenes.id))
  formulario = GaleriasImagenesForm()
  return render_to_response('galeriasImagenes.html',{'formulario':formulario,'galeria':galeria}, context_instance=RequestContext(request))

@login_required(login_url='/')
def crop_galeriasImagenes(request,galeria,id_imagen):
  print galeria
  image = Imagenes.objects.get(id=id_imagen)
  if request.method == "POST":
    im = Image.open(image.imagen)
    box = (int(request.POST.get('x1')),int(request.POST.get('y1')),int(request.POST.get('x2')),int(request.POST.get('y2')))
    cropiado = im.crop(box)
    cropiado.save("CostaAlgarrobo/carga/" + str(image.imagen))
    image.ancho = image.imagen.width
    image.alto = image.imagen.height
    image.save()
    return HttpResponseRedirect('/galeriasImagenes/' + galeria)   
  return render_to_response('crop.html', {'image': image}, context_instance=RequestContext(request))

@login_required(login_url='/')
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

@login_required(login_url='/')
def galeriasVideos(request,video):
  # Secciones
  try:
    galeria_video = GaleriasVideos.objects.get(nombreGaleria=video)
  except:
    galeria_video = None
  if request.method == 'POST':
    formulario = VideoForm(request.POST,request.FILES)
    if formulario.is_valid():
      archivo_video = formulario.cleaned_data['video']
      if galeria_video == None:
        galeria_video = GaleriasVideos.objects.create(nombreGaleria=video)
        galeria_video.save()

      else:
        for galeria in galeria_video.videos.all():
          galeria.delete()

      video_creado = Videos.objects.create(video=archivo_video)
      galeria_video.videos.add(video_creado)
      video_creado.save()
      galeria_video.save()

  if galeria_video != None:
    for galeria in galeria_video.videos.all():
      gale_video = galeria

    formulario = VideoForm(initial={'video':gale_video.video})
  else:
    formulario = VideoForm()

  return render_to_response('galeriasVideos.html',{'formulario':formulario}, context_instance=RequestContext(request))

def login_admin(request):
  if request.method == 'POST':
    formulario = AuthenticationForm(request.POST)
    if formulario.is_valid:
      usuario = request.POST['username']
      clave = request.POST['password']
      usuario = usuario.lower()
      acceso = authenticate(username=usuario, password=clave)
      if acceso is not None:
        if acceso.is_superuser:
          login(request,acceso)
          return HttpResponseRedirect('/background/home')
        else:
          formulario = AuthenticationForm()
          error_log = "Error"
          return render_to_response('index.html',{'formulario':formulario,'error_log':error_log}, context_instance=RequestContext(request))
      else:
        formulario = AuthenticationForm()
        error_log = "Username o contrasena incorrectos"
        return render_to_response('index.html',{'formulario':formulario,'error_log':error_log}, context_instance=RequestContext(request))
  else:
    formulario = AuthenticationForm()
  return render_to_response('index.html',{'formulario':formulario}, context_instance=RequestContext(request))
