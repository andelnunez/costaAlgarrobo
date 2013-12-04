from manager.models import *
from django.contrib import admin
from django.shortcuts import redirect
from admin_views.admin import AdminViews
from django.core.exceptions import ValidationError

class BackgroundAdmin(AdminViews):
    exclude = ['imagen']
    list_display = ('nombre', 'asociada')
    admin_views = (
      ('Subir Background', '/admin/background/home'),
    )

class ImagenAdmin(AdminViews):
    exclude = ['imagen']
    admin_views = (
      ('Subir Imagen a Galeria', '/galeriasImagenes/home'),
    )
    list_display = ('nombre', 'galeria')
    search_fields = ['nombre', 'galeria__nombreGaleria']

class PlanosAdmin(AdminViews):
    exclude = ['imagen']
    admin_views = (
      ('Subir Plano', '/galeriasImagenes/home'),
    )

class TipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edificio')
    search_fields = ['nombre', 'edificio__nombre']

class TextoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'seccion')
    search_fields = ['titulo', 'seccion__nombre']

admin.site.register(Edificio)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Background, BackgroundAdmin)
admin.site.register(Planos)
admin.site.register(Imagenes, ImagenAdmin)
admin.site.register(GaleriasImagenes)
admin.site.register(GaleriasPdf)
admin.site.register(Pdf)
admin.site.register(Videos)
admin.site.register(GaleriasVideos)
admin.site.register(Seccion)
admin.site.register(Texto, TextoAdmin)
admin.site.register(SubSeccion)
admin.site.register(ImagenesTransparente)
