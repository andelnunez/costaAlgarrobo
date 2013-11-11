from manager.models import *
from django.contrib import admin
from django.shortcuts import redirect
from admin_views.admin import AdminViews

class BackgroundAdmin(AdminViews):
    exclude = ['imagen']
    admin_views = (
      ('Subir Background', '/background/home'),
    )


admin.site.register(Background, BackgroundAdmin)
admin.site.register(Planos)
admin.site.register(Imagenes)
admin.site.register(GaleriasImagenes)
admin.site.register(GaleriasPdf)
admin.site.register(Pdf)
admin.site.register(Videos)
admin.site.register(GaleriasVideos)
admin.site.register(Seccion)
admin.site.register(Texto)
admin.site.register(SubSeccion)