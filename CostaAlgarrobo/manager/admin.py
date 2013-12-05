from manager.models import *
from django.contrib import admin
from django.shortcuts import redirect
from admin_views.admin import AdminViews
from django.core.exceptions import ValidationError

class BackgroundAdmin(AdminViews):
    exclude = ['ancho', 'alto']
    list_display = ('nombre', 'asociada')
    search_fields = ['nombre', 'asociada']
    admin_views = (
      ('Subir fondo que requiera recortar', '/admin/background/home'),
    )

class ImagenAdmin(AdminViews):
    exclude = ['size1', 'size2', 'alto', 'ancho']
    admin_views = (
      ('Subir Imagen a galeria que requiera recortar', '/galeriasImagenes/home'),
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
    exclude = ['seccion']
    list_display = ('titulo', 'seccion')
    search_fields = ['titulo', 'seccion__nombre']

class GaleriaAdmin(admin.ModelAdmin):
    search_fields = ['nombreGaleria']

class GaleriaPdfAdmin(admin.ModelAdmin):
    search_fields = ['nombreGaleria']

class VideosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')
    search_fields = ['nombre']

class TransparentesAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

#admin.site.register(Edificio)
#admin.site.register(Tipo, TipoAdmin)
admin.site.register(Background, BackgroundAdmin)
#admin.site.register(Planos)
admin.site.register(Imagenes, ImagenAdmin)
admin.site.register(GaleriasImagenes, GaleriaAdmin)
admin.site.register(Promocion)
admin.site.register(Videos, VideosAdmin)
#admin.site.register(GaleriasVideos)
admin.site.register(Seccion)
admin.site.register(Texto, TextoAdmin)
admin.site.register(SubSeccion)
admin.site.register(ImagenesTransparente, TransparentesAdmin)
