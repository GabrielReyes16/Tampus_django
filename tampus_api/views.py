from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import *
from rest_framework.views import APIView

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

#Views de Institucion
class InstitucionView(APIView):
     def get(self, request):
          instituciones = Institucion.objects.all()
          serializer = InstitucionSerializers(instituciones, many=True)
          return Response(serializer.data)

     def post(self, request):
          serializer = InstitucionSerializers(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InstitucionDetail(APIView):
     def get_object(self, pk):
          try:
               return Institucion.objects.get(pk=pk)
          except Institucion.DoesNotExist:
               raise Http404
     
     def get(self, request, pk):
          institucion = self.get_object(pk)
          serializer = InstitucionSerializers(institucion)
          return Response(serializer.data)
     
     def put(self, request, pk):
          institucion = self.get_object(pk)
          serializer = InstitucionSerializers(institucion, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     def delete(self, request, pk):
          institucion = self.get_object(pk)
          institucion.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)

#Views de Perfil
class PerfilView(APIView):
     def get(self, request):
          perfiles = Perfil.objects.all()
          serializer = PerfilSerializers(perfiles, many=True)
          return Response(serializer.data)

     def post(self, request):
          serializer = PerfilSerializers(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
class PerfilDetail(APIView):
     def get_object(self, pk):
          try:
               return Perfil.objects.get(pk=pk)
          except Perfil.DoesNotExist:
               raise Http404
     
     def get(self, request, pk):
          perfil = self.get_object(pk)
          serializer = PerfilSerializers(perfil)
          return Response(serializer.data)
     
     def put(self, request, pk):
          perfil = self.get_object(pk)
          serializer = PerfilSerializers(perfil, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     def delete(self, request, pk):
          perfil = self.get_object(pk)
          perfil.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)

#Views de Anuncio
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

#Views de Imagenes
class ImagenesView(APIView):
     def get(self, request):
          imagenes = Imagenes.objects.all()
          serializer = ImagenesSerializers(imagenes, many=True)
          return Response(serializer.data)

     def post(self, request):
          serializer = ImagenesSerializers(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
class ImagenesDetail(APIView):
     def get_object(self, pk):
          try:
               return Imagenes.objects.get(pk=pk)
          except Imagenes.DoesNotExist:
               raise Http404
     
     def get(self, request, pk):
          imagen = self.get_object(pk)
          serializer = ImagenesSerializers(imagen)
          return Response(serializer.data)
     
     def put(self, request, pk):
          imagen = self.get_object(pk)
          serializer = ImagenesSerializers(imagen, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     def delete(self, request, pk):
          imagen = self.get_object(pk)
          imagen.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
     
#Views de Anuncio_Etiqueta
class AnuncioEtiquetaView(APIView):
     def get(self, request):
          anuncio_etiquetas = Anuncio_Etiqueta.objects.all()
          serializer = Anuncio_EtiquetaSerializers(anuncio_etiquetas, many=True)
          return Response(serializer.data)

     def post(self, request):
          serializer = Anuncio_EtiquetaSerializers(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
class AnuncioEtiquetaDetail(APIView):
     def get_object(self, pk):
          try:
               return Anuncio_Etiqueta.objects.get(pk=pk)
          except Anuncio_Etiqueta.DoesNotExist:
               raise Http404
     
     def get(self, request, pk):
          anuncio_etiqueta = self.get_object(pk)
          serializer = Anuncio_EtiquetaSerializers(anuncio_etiqueta)
          return Response(serializer.data)
     
     def put(self, request, pk):
          anuncio_etiqueta = self.get_object(pk)
          serializer = Anuncio_EtiquetaSerializers(anuncio_etiqueta, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     def delete(self, request, pk):
          anuncio_etiqueta = self.get_object(pk)
          anuncio_etiqueta.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
     
#Views de Perfil_Imagen
class PerfilImagenView(APIView):
     def get(self, request):
          perfil_imagenes = Perfil_Imagen.objects.all()
          serializer = Perfil_ImagenSerializers(perfil_imagenes, many=True)
          return Response(serializer.data)

     def post(self, request):
          serializer = Perfil_ImagenSerializers(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PerfilImagenDetail(APIView):
     def get_object(self, pk):
          try:
               return Perfil_Imagen.objects.get(pk=pk)
          except Perfil_Imagen.DoesNotExist:
               raise Http404
     
     def get(self, request, pk):
          perfil_imagen = self.get_object(pk)
          serializer = Perfil_ImagenSerializers(perfil_imagen)
          return Response(serializer.data)
     
     def put(self, request, pk):
          perfil_imagen = self.get_object(pk)
          serializer = Perfil_ImagenSerializers(perfil_imagen, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     def delete(self, request, pk):
          perfil_imagen = self.get_object(pk)
          perfil_imagen.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
     
#Views de Etiqueta
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