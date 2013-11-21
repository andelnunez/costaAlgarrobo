from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from CostaAlgarrobo import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'manager.views.login_admin'),
    url(r'^admin/background/(?P<seccion>.*)$', 'manager.views.background'),
    # url(r'^CostaAlgarrobo/', include('CostaAlgarrobo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),

    url(r'^background/(?P<seccion>.*)$', 'manager.views.background'),
    url(r'^planos/(?P<edif>.*)$', 'manager.views.planos'),
    url(r'^galeriasImagenes/(?P<gale>.*)$', 'manager.views.galeriasImagenes'),
    url(r'^carga_pdf/(?P<pdf>.*)$', 'manager.views.carga_pdf'),
    url(r'^galeriasVideos/(?P<video>.*)$', 'manager.views.galeriasVideos'),
    url(r'^crop_background/(?P<id_back>.*)$', 'manager.views.crop_background'),
    url(r'^crop_planos/(?P<id_plano>.*)$', 'manager.views.crop_planos'), 
    url(r'^crop_galeriasImagenes/(?P<galeria>.*)/(?P<id_imagen>.*)$', 'manager.views.crop_galeriasImagenes'),
    url(r'^texto/(?P<id_seccion>.*)$', 'manager.views.texto'),
    url(r'^descripcion/$', 'manager.views.descripcion'),
    url(r'^departamentos/$', 'manager.views.departamentos'),
    url(r'^equipamento/$', 'manager.views.equipamento'),
    url(r'^infraestructura/$', 'manager.views.infraestructura'),
    url(r'^fotos_piloto/$', 'manager.views.fotos_piloto'),
    url(r'^plantas/$', 'manager.views.plantas'),
    url(r'^foto/$', 'manager.views.foto'),
    url(r'^video/$', 'manager.views.video'),
    url(r'^contactanos/$', 'manager.views.contactanos'),
    url(r'^etapa1/$', 'manager.views.etapa1'),
    url(r'^etapa2/$', 'manager.views.etapa2'),
    url(r'^ubicacion/$', 'manager.views.ubicacion'),
    url(r'^oferta/$', 'manager.views.oferta'),
)
