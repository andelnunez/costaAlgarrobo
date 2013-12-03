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
from django.core.mail import EmailMessage, EmailMultiAlternatives




@login_required(login_url='/')
def background(request,seccion):
  # Secciones
  try:
    secciones = Seccion.objects.all()
  except:
    secciones = None
  if request.method == 'POST':
    formulario = BackgroundForm(request.POST,request.FILES)
    if formulario.is_valid():
      nombre = formulario.cleaned_data['nombre']
      imagen = formulario.cleaned_data['imagen']
      alineacion1 = formulario.cleaned_data['alineacion1']
      alineacion2 = formulario.cleaned_data['alineacion2']
      secciones = formulario.cleaned_data['seccion']
      print alineacion1


#      if sec == None:
      sec = Background.objects.create(nombre=nombre,imagen=imagen,vertical=alineacion1,horizontal=alineacion2)
      for seccion in secciones:
        sec.seccion.add(seccion)
      sec.save()
#      sec.ancho = sec.imagen.width
#      sec.alto = sec.imagen.height
#      sec.save()
#      else:
#        if request.POST.get('imagen-clear') == 'on':
#          imagen = None
#          sec.imagen = None
#        if imagen != None:
#          sec.imagen = imagen
#      sec.alineacion1 = alineacion1
#      sec.alineacion2 = alineacion2
#      sec.size1 = size1
#      sec.size2 = size2
#      sec.save()
#        if imagen != None:
#      sec.ancho = sec.imagen.width
#      sec.alto = sec.imagen.height
#      sec.save()
      # Crop
      return HttpResponseRedirect('/crop_background/' + str(sec.id))
#  if sec != None:
#    formulario = BackgroundForm(initial={'alineacion1':sec.alineacion1,'alineacion2':sec.alineacion2,'size1':sec.size1,'size2':sec.size2})

  else:
    formulario = BackgroundForm()
  return render_to_response('background.html', {'actual': seccion, 'secciones': secciones, 'formulario': formulario}, context_instance=RequestContext(request))

@login_required(login_url='/')
def crop_background(request,id_back):
  image = Background.objects.get(id=id_back)
  if request.method == "POST":
    im = Image.open(image.imagen)
    if not((request.POST.get('x1') == "") or (request.POST.get('y1') == "") or (request.POST.get('x2') == "") or (request.POST.get('y2') == "")):
      box = (int(request.POST.get('x1')),int(request.POST.get('y1')),int(request.POST.get('x2')),int(request.POST.get('y2')))
      cropiado = im.crop(box)
      cropiado.save("CostaAlgarrobo/carga/" + str(image.imagen))
    image.ancho = image.imagen.width
    image.alto = image.imagen.height
    image.save()

    return HttpResponseRedirect('/admin/manager/background/')
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
    if not((request.POST.get('x1') == "") or (request.POST.get('y1') == "") or (request.POST.get('x2') == "") or (request.POST.get('y2') == "")):
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
  galerias = GaleriasImagenes.objects.all()
  if request.method == 'POST':
    formulario = GaleriasImagenesForm(request.POST,request.FILES)
    if formulario.is_valid():
      nombre = formulario.cleaned_data['nombre']
      imagen = formulario.cleaned_data['imagenes']
      alineacion1 = formulario.cleaned_data['alineacion1']
      alineacion2 = formulario.cleaned_data['alineacion2']
      size1 = formulario.cleaned_data['size1']
      size2 = formulario.cleaned_data['size2']
      imagenes = Imagenes.objects.create(galeria=galeria, nombre=nombre, imagen=imagen,alineacion1=alineacion1,alineacion2=alineacion2,size1=size1,size2=size2)
      imagenes.save()
      #Agregando ManyToMany
      galeria.save()
      return HttpResponseRedirect('/crop_galeriasImagenes/' + gale + '/' + str(imagenes.id))
  else:
    formulario = GaleriasImagenesForm()
  return render_to_response('galeriasImagenes.html', {'galerias': galerias, 'formulario':formulario,'galeria':galeria}, context_instance=RequestContext(request))

@login_required(login_url='/')
def crop_galeriasImagenes(request,galeria,id_imagen):
  print galeria
  image = Imagenes.objects.get(id=id_imagen)
  if request.method == "POST":
    im = Image.open(image.imagen)
    if not((request.POST.get('x1') == "") or (request.POST.get('y1') == "") or (request.POST.get('x2') == "") or (request.POST.get('y2') == "")):
      box = (int(request.POST.get('x1')),int(request.POST.get('y1')),int(request.POST.get('x2')),int(request.POST.get('y2')))
      cropiado = im.crop(box)
      cropiado.save("CostaAlgarrobo/carga/" + str(image.imagen))
    image.ancho = image.imagen.width
    image.alto = image.imagen.height
    image.save()
    return HttpResponseRedirect('/admin/manager/imagenes/')
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
  try:
    seccion = Seccion.objects.get(nombre="Home")
    fondos = Background.objects.filter(seccion=seccion)
  except:
    fondos = ""

 # print current_url
  return render_to_response('index.html',{'fondos': fondos}, context_instance=RequestContext(request))

def oferta(request):
  request.session['oferta'] = False
  return HttpResponseRedirect(request.session['url'])

@login_required(login_url='/')
def texto(request, id_seccion):
  seccion = Seccion.objects.get(pk=id_seccion)
  textos = Texto.objects.filter(seccion__seccion=seccion)
  subsecciones = SubSeccion.objects.filter(seccion=seccion)
  if request.method == 'POST':
    formulario = TextoForm(request.POST)
    if formulario.is_valid():
      formulario.save()
      return HttpResponseRedirect('/texto')
  else:
    formulario = TextoForm()
  return render_to_response('texto.html',{'textos':textos, 'formulario':formulario}, context_instance=RequestContext(request))

def descripcion(request):
  texto = ""
  titulo = ""
  try:
    seccion = Seccion.objects.get(nombre="Descripcion")
    subseccion = SubSeccion.objects.get(nombre="Proyecto Descripcion")
    texto = Texto.objects.get(seccion = subseccion)
    fondos = Background.objects.filter(seccion=seccion)
    text = Texto.objects.get(seccion = subseccion)
    texto = text.texto
    titulo = text.titulo
  except:
    fondos = ""
  return render_to_response('descripcion.html', {'texto': texto, 'titulo': titulo}, context_instance=RequestContext(request))

def departamentos(request):
  texto = ""
  titulo = ""
  try:
    seccion = Seccion.objects.get(nombre="Departamentos")
    fondos = Background.objects.filter(seccion=seccion)
    #########################################3
    subSeccion = SubSeccion.objects.get(nombre="Proyecto Departamento")
    textos = Texto.objects.filter(seccion=subSeccion)
    if len(textos) > 0:
      for tex in textos:
        texto = tex.texto
        titulo = tex.titulo
  except:
    fondos = ""
  return render_to_response('departamentos.html',{'texto':texto,'titulo':titulo},context_instance=RequestContext(request))

def equipamento(request):
  texto = ""
  titulo = ""
  try:
    seccion = Seccion.objects.get(nombre="Equipamiento")
    fondos = Background.objects.filter(seccion=seccion)
    subseccion = SubSeccion.objects.get(nombre="Proyecto Equipamiento")
    text = Texto.objects.get(seccion = subseccion)
    texto = text.texto
    titulo = text.titulo
  except:
    fondos = ""
  return render_to_response('equipamento.html', {'texto': texto, 'titulo': titulo}, context_instance=RequestContext(request))

def infraestructura(request):
  texto = ""
  titulo = ""
  try:
    seccion = Seccion.objects.get(nombre="Infraestructura")
    fondos = Background.objects.filter(seccion=seccion)
    subseccion = SubSeccion.objects.get(nombre="Proyecto Infraestructura")
    text = Texto.objects.get(seccion = subseccion)
    texto = text.texto
    titulo = text.titulo
  except:
    fondos = ""
  return render_to_response('infraestructura.html', {'texto': texto, 'titulo': titulo}, context_instance=RequestContext(request))

def fotos_piloto(request):
  imagenes_mar = []
  imagenes_bosque = []
  try:
    seccion = Seccion.objects.get(nombre="Fotos Piloto")
    fondos = Background.objects.filter(seccion=seccion)
    galeria_mar = GaleriasImagenes.objects.get(nombreGaleria="Mar")
    galeria_bosque = GaleriasImagenes.objects.get(nombreGaleria="Bosque")
    imagenes_mar = Imagenes.objects.filter(galeria=galeria_mar)
    imagenes_bosque = Imagenes.objects.filter(galeria=galeria_bosque)
  except:
    fondos = ""
  return render_to_response('fotos_piloto.html',{'imagenes_mar':imagenes_mar,'imagenes_bosque':imagenes_bosque},context_instance=RequestContext(request))

def plantas(request):
  try:
    fondos = Background.objects.filter(seccion=seccion)


  except:
    fondos = ""
  return render_to_response('plantas.html',context_instance=RequestContext(request))

def foto(request, id_galeria):
  galerias = GaleriasImagenes.objects.all()
  imagenes = []
  try:
    galeria = GaleriasImagenes.objects.get(id=id_galeria)
    imagenes = Imagenes.objects.filter(galeria=galeria)
  except:
    if galerias.count() == 0:
      pass
    else:
      galeria = galerias[0].id
      imagenes = Imagenes.objects.filter(galeria=galeria)

  return render_to_response('foto.html', {'imagenes': imagenes, 'galerias': galerias}, context_instance=RequestContext(request))

def video(request):
  return render_to_response('video.html',context_instance=RequestContext(request))

def contactanos(request):
  if request.method == 'POST':
    formulario = ContactoForm(request.POST)
    if formulario.is_valid():
      titulo = 'Contacto'
      contenido = 'Nombre: ' + formulario.cleaned_data['nombre'] + '\n'
      contenido += 'Rut: ' + formulario.cleaned_data['rut'] + '\n'
      contenido += 'Direccion: ' + formulario.cleaned_data['direccion'] + '\n'
      contenido += 'Telefono: ' + str(formulario.cleaned_data['telefono']) + '\n'
      contenido += 'Celular: ' + str(formulario.cleaned_data['celular']) + '\n'
      contenido += 'Email: ' + formulario.cleaned_data['email'] + '\n'
      contenido += 'Consulta: ' + formulario.cleaned_data['consulta'] + '\n'
      correo = EmailMessage(titulo, contenido, to=['leonardogutierrezh@gmail.com'])
      correo.send()
  else:
    formulario = ContactoForm()
  return render_to_response('contactanos.html', {'formulario': formulario}, context_instance=RequestContext(request))

def etapa1(request):
  return render_to_response('etapa1.html',context_instance=RequestContext(request))

def etapa2(request):
  return render_to_response('etapa2.html',context_instance=RequestContext(request))

def ubicacion(request):
  return render_to_response('ubicacion.html',context_instance=RequestContext(request))

def equipo(request):
  return render_to_response('avance.html',context_instance=RequestContext(request))

def avance(request):
  return render_to_response('equipo.html',context_instance=RequestContext(request))

def cotizacion(request):
  return render_to_response('cotizacion.html',context_instance=RequestContext(request))

def mar(request):
  return render_to_response('mar.html',context_instance=RequestContext(request))

def bosque(request):
  return render_to_response('bosque.html',context_instance=RequestContext(request))
