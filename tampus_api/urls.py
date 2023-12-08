from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import path

urlpatterns = [
        path('user/get', UsuariosView.as_view()),
        path('user/post', UsuariosView.as_view()),
        path('user/get/<int:pk>/', UsuariosDetail.as_view()),
        path('user/put/<int:pk>/', UsuariosDetail.as_view()),
        path('user/delete/<int:pk>/', UsuariosDetail.as_view()),
        # Institucion urls
        path('institucion/get', InstitucionView.as_view()),
        path('institucion/post', InstitucionView.as_view()),
        path('institucion/get/<int:pk>/', InstitucionDetail.as_view()),
        path('institucion/put/<int:pk>/', InstitucionDetail.as_view()),
        path('institucion/delete/<int:pk>/', InstitucionDetail.as_view()),
        # Perfil urls
        path('perfil/get', PerfilView.as_view()),
        path('perfil/post', PerfilView.as_view()),
        path('perfil/get/<int:pk>/', PerfilDetail.as_view()),
        path('perfil/put/<int:pk>/', PerfilDetail.as_view()),
        path('perfil/delete/<int:pk>/', PerfilDetail.as_view()),
        # Anuncio urls
        path('anuncio/get', AnuncioView.as_view()),
        path('anuncio/post', AnuncioView.as_view()),
        path('anuncio/get/<int:pk>/', AnuncioDetail.as_view()),
        path('anuncio/put/<int:pk>/', AnuncioDetail.as_view()),
        path('anuncio/delete/<int:pk>/', AnuncioDetail.as_view()),
        # Imagenes urls
        path('imagenes/get', ImagenesView.as_view()),
        path('imagenes/post', ImagenesView.as_view()),
        path('imagenes/get/<int:pk>/', ImagenesDetail.as_view()),
        path('imagenes/put/<int:pk>/', ImagenesDetail.as_view()),
        path('imagenes/delete/<int:pk>/', ImagenesDetail.as_view()),
        # AnuncioEtiqueta urls
        path('anuncio_etiqueta/get', AnuncioEtiquetaView.as_view()),
        path('anuncio_etiqueta/post', AnuncioEtiquetaView.as_view()),
        path('anuncio_etiqueta/get/<int:pk>/', AnuncioEtiquetaDetail.as_view()),
        path('anuncio_etiqueta/put/<int:pk>/', AnuncioEtiquetaDetail.as_view()),
        path('anuncio_etiqueta/delete/<int:pk>/', AnuncioEtiquetaDetail.as_view()),
        # Perfil_Imagen urls
        path('perfil_imagen/get', PerfilImagenView.as_view()),
        path('perfil_imagen/post', PerfilImagenView.as_view()),
        path('perfil_imagen/get/<int:pk>/', PerfilImagenDetail.as_view()),
        path('perfil_imagen/put/<int:pk>/', PerfilImagenDetail.as_view()),
        path('perfil_imagen/delete/<int:pk>/', PerfilImagenDetail.as_view()),
        # Etiqueta urls
        path('etiqueta/get', EtiquetaView.as_view()),
        path('etiqueta/post', EtiquetaView.as_view()),
        path('etiqueta/get/<int:pk>/', EtiquetaDetail.as_view()),
        path('etiqueta/put/<int:pk>/', EtiquetaDetail.as_view()),
        path('etiqueta/delete/<int:pk>/', EtiquetaDetail.as_view()),
    ]