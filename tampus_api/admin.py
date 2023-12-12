from django.contrib import admin
from tampus_api.models import Usuarios, Etiqueta, Anuncio, AnuncioEtiqueta, Favoritos

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Etiqueta)
admin.site.register(Anuncio)
admin.site.register(AnuncioEtiqueta)
admin.site.register(Favoritos)
