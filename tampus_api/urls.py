from django.contrib import admin
from django.urls import path
from .views import (UsuariosView, UsuariosDetail, AnuncioView, AnuncioDetail, AnuncioEtiquetaView, AnuncioEtiquetaDetail, EtiquetaView, EtiquetaDetail, FavoritosView, FavoritosDetail, AnuncioFilesView, AnuncioFilesDetail, FileDetailsView, FileDetailsDetail)
from django.urls import path

urlpatterns = [
        # User urls
        path('user/get', UsuariosView.as_view()),
        path('user/post', UsuariosView.as_view()),
        path('user/get/<int:pk>/', UsuariosDetail.as_view()),
        path('user/put/<int:pk>/', UsuariosDetail.as_view()),
        path('user/delete/<int:pk>/', UsuariosDetail.as_view()),
        # Anuncio urls
        path('anuncio/get', AnuncioView.as_view()),
        path('anuncio/post', AnuncioView.as_view()),
        path('anuncio/get/<int:pk>/', AnuncioDetail.as_view()),
        path('anuncio/put/<int:pk>/', AnuncioDetail.as_view()),
        path('anuncio/delete/<int:pk>/', AnuncioDetail.as_view()),
        # AnuncioEtiqueta urls
        path('anuncio_etiqueta/get', AnuncioEtiquetaView.as_view()),
        path('anuncio_etiqueta/post', AnuncioEtiquetaView.as_view()),
        path('anuncio_etiqueta/get/<int:pk>/', AnuncioEtiquetaDetail.as_view()),
        path('anuncio_etiqueta/put/<int:pk>/', AnuncioEtiquetaDetail.as_view()),
        path('anuncio_etiqueta/delete/<int:pk>/', AnuncioEtiquetaDetail.as_view()),
        # AnuncioFiles urls
        path('anuncio_files/get', AnuncioFilesView.as_view()),
        path('anuncio_files/post', AnuncioFilesView.as_view()),
        path('anuncio_files/get/<int:pk>/', AnuncioFilesDetail.as_view()),
        path('anuncio_files/put/<int:pk>/', AnuncioFilesDetail.as_view()),
        path('anuncio_files/delete/<int:pk>/', AnuncioFilesDetail.as_view()),
        # FileDetails urls
        path('file_details/get', FileDetailsView.as_view()),
        path('file_details/post', FileDetailsView.as_view()),
        path('file_details/get/<int:pk>/', FileDetailsDetail.as_view()),
        path('file_details/put/<int:pk>/', FileDetailsDetail.as_view()),
        path('file_details/delete/<int:pk>/', FileDetailsDetail.as_view()),
        # Etiqueta urls
        path('etiqueta/get', EtiquetaView.as_view()),
        path('etiqueta/post', EtiquetaView.as_view()),
        path('etiqueta/get/<int:pk>/', EtiquetaDetail.as_view()),
        path('etiqueta/put/<int:pk>/', EtiquetaDetail.as_view()),
        path('etiqueta/delete/<int:pk>/', EtiquetaDetail.as_view()),
        # Favoritos urls
        path('favoritos/get', FavoritosView.as_view()),
        path('favoritos/post', FavoritosView.as_view()),
        path('favoritos/get/<int:pk>/', FavoritosDetail.as_view()),
        path('favoritos/put/<int:pk>/', FavoritosDetail.as_view()),
        path('favoritos/delete/<int:pk>/', FavoritosDetail.as_view()),
    ]
