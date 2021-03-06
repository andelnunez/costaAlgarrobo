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
from django.core.urlresolvers import resolve

def cookie_oferta(request):
  ofertas = Promocion.objects.all()
  if ofertas.count() > 0:
    info_oferta = ofertas[0]
  else:
    info_oferta = ""
  if 'oferta' in request.session:
    oferta = request.session['oferta']
  else:
    oferta = request.session['oferta'] = True
  current_url = request.path
  if current_url == "/oferta/":
    pass
  else:
    request.session['url'] = current_url
  return {'oferta': oferta, 'info_oferta': info_oferta,}