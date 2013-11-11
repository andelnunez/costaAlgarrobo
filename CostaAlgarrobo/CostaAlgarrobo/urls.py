from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from CostaAlgarrobo import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'manager.views.login_admin'),
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

)