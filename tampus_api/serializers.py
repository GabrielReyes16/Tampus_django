from rest_framework import serializers
from .models import  Usuarios, Institucion, Perfil, Anuncio, Imagenes, Anuncio_Etiqueta, Perfil_Imagen, Etiqueta, Anuncio_Etiqueta

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class InstitucionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'

class PerfilSerializers(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class AnuncioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = '__all__'  

class ImagenesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = '__all__'

class Perfil_ImagenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Perfil_Imagen
        fields = '__all__'

class EtiquetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'

class Anuncio_EtiquetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anuncio_Etiqueta
        fields = '__all__'  