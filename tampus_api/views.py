from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import UsuariosSerializers, AnuncioSerializers, AnuncioEtiquetaSerializers, EtiquetaSerializers, \
    FileDetailsSerializers, AnuncioFilesSerializers, FavoritosSerializers
from rest_framework.views import APIView
from .models import Usuarios, Anuncio, AnuncioEtiqueta, Etiqueta, Favoritos, FileDetails, AnuncioFiles


# Create your views here.


class UsuariosView(APIView):
    def get(self, request):
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializers(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuariosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuariosDetail(APIView):
    def get_object(self, pk):
        try:
            return Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        usuario = self.get_object(pk)
        serializer = UsuariosSerializers(usuario)
        return Response(serializer.data)

    def put(self, request, pk):
        usuario = self.get_object(pk)
        serializer = UsuariosSerializers(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Views de Anuncio
class AnuncioView(APIView):
    def get(self, request):
        anuncios = Anuncio.objects.all()
        serializer = AnuncioSerializers(anuncios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnuncioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnuncioDetail(APIView):
    def get_object(self, pk):
        try:
            return Anuncio.objects.get(pk=pk)
        except Anuncio.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        anuncio = self.get_object(pk)
        serializer = AnuncioSerializers(anuncio)
        return Response(serializer.data)

    def put(self, request, pk):
        anuncio = self.get_object(pk)
        serializer = AnuncioSerializers(anuncio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        anuncio = self.get_object(pk)
        anuncio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Views de Anuncio_Etiqueta
class AnuncioEtiquetaView(APIView):
    def get(self, request):
        anuncio_etiquetas = AnuncioEtiqueta.objects.all()
        serializer = AnuncioEtiquetaSerializers(anuncio_etiquetas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnuncioEtiquetaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnuncioEtiquetaDetail(APIView):
    def get_object(self, pk):
        try:
            return AnuncioEtiqueta.objects.get(pk=pk)
        except Anuncio_Etiqueta.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        anuncio_etiqueta = self.get_object(pk)
        serializer = AnuncioEtiquetaSerializers(anuncio_etiqueta)
        return Response(serializer.data)

    def put(self, request, pk):
        anuncio_etiqueta = self.get_object(pk)
        serializer = AnuncioEtiquetaSerializers(anuncio_etiqueta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        anuncio_etiqueta = self.get_object(pk)
        anuncio_etiqueta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Views de Etiqueta
class EtiquetaView(APIView):
    def get(self, request):
        etiquetas = Etiqueta.objects.all()
        serializer = EtiquetaSerializers(etiquetas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EtiquetaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EtiquetaDetail(APIView):
    def get_object(self, pk):
        try:
            return Etiqueta.objects.get(pk=pk)
        except Etiqueta.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        etiqueta = self.get_object(pk)
        serializer = EtiquetaSerializers(etiqueta)
        return Response(serializer.data)

    def put(self, request, pk):
        etiqueta = self.get_object(pk)
        serializer = EtiquetaSerializers(etiqueta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        etiqueta = self.get_object(pk)
        etiqueta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FavoritosView(APIView):
    def get(self, request):
        favoritos = Favoritos.objects.all()
        serializer = FavoritosSerializers(favoritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FavoritosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoritosDetail(APIView):
    def get_object(self, pk):
        try:
            return Favoritos.objects.get(pk=pk)
        except Favoritos.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        favoritos = self.get_object(pk)
        serializer = FavoritosSerializers(favoritos)
        return Response(serializer.data)

    def put(self, request, pk):
        favoritos = self.get_object(pk)
        serializer = FavoritosSerializers(favoritos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        favoritos = self.get_object(pk)
        favoritos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnuncioFilesView(APIView):
    def get(self, request):
        anuncio_files = AnuncioFiles.objects.all()
        serializer = AnuncioFilesSerializers(anuncio_files, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnuncioFilesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnuncioFilesDetail(APIView):
    def get_object(self, pk):
        try:
            return AnuncioFiles.objects.get(pk=pk)
        except AnuncioFiles.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        anuncio_files = self.get_object(pk)
        serializer = AnuncioFilesSerializers(anuncio_files)
        return Response(serializer.data)

    def put(self, request, pk):
        anuncio_files = self.get_object(pk)
        serializer = AnuncioFilesSerializers(anuncio_files, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        anuncio_files = self.get_object(pk)
        anuncio_files.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FileDetailsView(APIView):
    def get(self, request):
        file_details = FileDetails.objects.all()
        serializer = FileDetailsSerializers(file_details, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FileDetailsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileDetailsDetail(APIView):
    def get_object(self, pk):
        try:
            return FileDetails.objects.get(pk=pk)
        except FileDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        file_details = self.get_object(pk)
        serializer = FileDetailsSerializers(file_details)
        return Response(serializer.data)

    def put(self, request, pk):
        file_details = self.get_object(pk)
        serializer = FileDetailsSerializers(file_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        file_details = self.get_object(pk)
        file_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
