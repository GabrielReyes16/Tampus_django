from django.db import models
from django.utils import timezone


# Create your models here.
class Usuarios(models.Model):
    estado_user = models.BooleanField(null=True)
    created_by = models.DateTimeField(default=timezone.now, null=True)
    fecha_nacimiento = models.DateTimeField(null=True)
    id = models.BigAutoField(primary_key=True)
    updated_by = models.DateTimeField(default=timezone.now, blank=True, null=True)
    apellido_usuario = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, unique=True, blank=True)
    nombre_usuario = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    ROLE_CHOICES = [
        ('ROLE_ANFITRION', 'Anfitrión'),
        ('ROLE_ESTUDIANTE', 'Estudiante'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True)
    telefono = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'usuarios'
        managed = True


class Etiqueta(models.Model):
    id_etiqueta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'etiqueta'
        managed = True


class FileDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_download_uri = models.CharField(max_length=255, blank=True)
    file_name = models.CharField(max_length=255, blank=True)
    file_size = models.BigIntegerField(null=True)
    file_uri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"FileDetails {self.id}"

    class Meta:
        db_table = 'file_details'


class Anuncio(models.Model):
    id_anuncio = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True)
    dimensiones = models.IntegerField(null=False)
    estado_anuncio = models.CharField(max_length=1, blank=True)
    num_cama = models.IntegerField(null=False)
    num_hab = models.IntegerField(null=False)
    precio = models.DecimalField(max_digits=38, decimal_places=2, null=True)
    proposito = models.CharField(max_length=50, blank=True)
    tipo_espacio = models.CharField(max_length=30, blank=True)
    titulo = models.CharField(max_length=30, blank=True)
    ubicacion = models.CharField(max_length=50, blank=True)
    id_user = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='id_user')
    created_by = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        db_table = 'anuncio'
        managed = True


class AnuncioEtiqueta(models.Model):
    id = models.AutoField(primary_key=True)
    id_anuncio = models.OneToOneField(Anuncio, on_delete=models.CASCADE, null=True, unique=True, db_column='id_anuncio')
    id_etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE, null=True, db_column='id_etiqueta')

    class Meta:
        db_table = 'anuncio_etiqueta'

    managed = True


class AnuncioFiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_anuncio = models.ForeignKey('Anuncio', on_delete=models.CASCADE, null=True, db_column='id_anuncio')
    id_file = models.ForeignKey(FileDetails, on_delete=models.CASCADE, null=True, db_column='id_file')

    def __str__(self):
        return f"AnuncioFiles {self.id}"

    class Meta:
        db_table = 'anuncio_files'
        indexes = [
            models.Index(fields=['id_anuncio']),
            models.Index(fields=['id_file']),
        ]


class Favoritos(models.Model):
    estado_favorito = models.BooleanField(null=False)
    fecha_creacion = models.DateField(null=True)
    id_anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, null=True, db_column='id_anuncio')
    id_favorito = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True, db_column='id_usuario')

    class Meta:
        db_table = 'favoritos'

    managed = True
