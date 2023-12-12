from rest_framework import serializers
from .models import Usuarios, Anuncio, AnuncioEtiqueta, Etiqueta, Favoritos, FileDetails, AnuncioFiles


class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'


class AnuncioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = '__all__'


class EtiquetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'


class AnuncioEtiquetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnuncioEtiqueta
        fields = '__all__'


class FavoritosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = '__all__'


class FileDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = FileDetails
        fields = '__all__'


class AnuncioFilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnuncioFiles
        fields = '__all__'
