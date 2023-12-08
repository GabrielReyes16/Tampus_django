from django.db import models

# Create your models here.
class Usuarios(models.Model):
  id = models.BigAutoField(primary_key=True)
  nombres = models.CharField(max_length=255)
  apellidos = models.CharField(max_length=255)
  email = models.CharField(max_length=255, unique=True)
  password = models.CharField(max_length=255)
  fecha_nacimiento = models.DateField(null=True)
  telefono = models.CharField(max_length=255)
  token = models.BigIntegerField()
  role = models.IntegerField()
  created_by = models.DateTimeField(auto_now_add=True)
  updated_by = models.DateTimeField(auto_now=True)
  estado_user = models.BooleanField()
  class Meta:
        # Opciones del modelo
        db_table = 'Usuarios'

class Institucion(models.Model):
  id_institucion = models.BigAutoField(primary_key=True)
  nombre = models.CharField(max_length=50, unique=True)
  direccion = models.CharField(max_length=50)
  class Meta:
        # Opciones del modelo
        db_table = 'Institucion'


class Perfil(models.Model):
  id = models.BigAutoField(primary_key=True)
  id_user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
  id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
  dni = models.CharField(max_length=8, null=True)
  carnet_extranjeria = models.CharField(max_length=20, null=True)

  class Meta:
    db_table = 'Perfil'
    constraints = [
      models.CheckConstraint(
        check=models.Q(dni__isnull=False, carnet_extranjeria__isnull=True) |
            models.Q(dni__isnull=True, carnet_extranjeria__isnull=False),
        name='ck_dni_or_carnet'
      ),
      models.CheckConstraint(
        check=models.Q(dni__regex=r'^[0-9]{8}$'),
        name='ck_dni_format'
      ),
      models.CheckConstraint(
        check=models.Q(carnet_extranjeria__regex=r'^[0-9]{6,12}$'),
        name='ck_carnet_format'
      )
    ]   


class Anuncio(models.Model):
  id_anuncio = models.BigAutoField(primary_key=True)
  id_user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
  proposito = models.CharField(max_length=50)
  titulo = models.CharField(max_length=30)
  descripcion = models.CharField(max_length=100)
  ubicacion = models.CharField(max_length=50)
  precio_min = models.DecimalField(max_digits=10, decimal_places=2)
  precio_max = models.DecimalField(max_digits=10, decimal_places=2)
  tipo_espacio = models.CharField(max_length=30)
  num_hab = models.IntegerField()
  num_cama = models.IntegerField()
  dimensiones = models.DecimalField(max_digits=10, decimal_places=2)
  estado_anuncio = models.CharField(max_length=1)

  class Meta:
    db_table = 'Anuncio'
    constraints = [
      models.CheckConstraint(
        check=models.Q(precio_max__gt=models.F('precio_min')),
        name='check_precio_max'
      ),
      models.CheckConstraint(
        check=models.Q(precio_max__gt=0) & models.Q(precio_min__gt=0),
        name='check_precio_positivo'
      )
    ]

class Imagenes(models.Model):
  id_imagen = models.IntegerField(primary_key=True)
  ruta = models.BinaryField()
  class Meta:
        # Opciones del modelo
        db_table = 'Imagenes'



class Anuncio_Imagen(models.Model):
  id = models.IntegerField(primary_key=True)
  id_anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
  id_imagen = models.ForeignKey(Imagenes, on_delete=models.CASCADE)
  class Meta:
        # Opciones del modelo
        db_table = 'Anuncio_Imagen'



class Perfil_Imagen(models.Model):
  id = models.IntegerField(primary_key=True)
  id_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
  id_imagen = models.ForeignKey(Imagenes, on_delete=models.CASCADE)
  class Meta:
        # Opciones del modelo
        db_table = 'Perfil_Imagen'


class Etiqueta(models.Model):
  id_etiqueta = models.IntegerField(primary_key=True)
  nombre = models.CharField(max_length=20)
  class Meta:
        # Opciones del modelo
        db_table = 'Etiqueta'


class Anuncio_Etiqueta(models.Model):
  id = models.IntegerField(primary_key=True)
  id_anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
  id_etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
  class Meta:
        # Opciones del modelo
        db_table = 'Anuncio_Etiqueta'



