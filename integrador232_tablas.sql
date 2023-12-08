#truncate
#drop TABLE etiqueta;
#drop TABLE usuarios;
#drop TABLE anuncio;
#drop TABLE anuncio_etiqueta;
#drop TABLE imagen;
#drop TABLE institucion;
#drop TABLE perfil;
#drop table anuncio_imagen;

-- Tabla de Usuarios
CREATE TABLE Usuarios (
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombres` VARCHAR(255),
    `apellidos` VARCHAR(255),
    `email` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `fecha_nacimiento` DATE,
    `telefono` VARCHAR(255),
    `token` BIGINT,
    `role` INT,
    `created_by` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_by` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `estado_user` BOOLEAN,
    CONSTRAINT uk_email UNIQUE (email)
);
INSERT INTO Usuarios (nombres, apellidos, email, password, fecha_nacimiento, telefono, token, role, created_by, updated_by, estado_user)
VALUES
  ('Juan', 'Perez', 'juan@example.com', 'password123', '1990-01-01', '123456789', 1234567890, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1),
  ('Maria', 'Lopez', 'maria@example.com', 'password456', '1995-02-15', '987654321', 9876543210, 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1),
  ('Pedro', 'Gomez', 'pedro@example.com', 'password789', '1985-06-30', '555555555', 5555555555, 3, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1);
-- Tabla de Usuarios
{
  "usuarios": [
    {
      "id": 1,
      "nombres": "Luis",
      "apellidos": "González",
      "email": "luis@example.com",
      "password": "pass123",
      "fecha_nacimiento": "1992-05-10",
      "telefono": "987654321",
      "token": 1234567890,
      "role": 1,
      "created_by": "2022-01-01T10:00:00Z",
      "updated_by": "2022-01-01T10:00:00Z",
      "estado_user": true
    },
    {
      "id": 2,
      "nombres": "Ana",
      "apellidos": "Martínez",
      "email": "ana@example.com",
      "password": "pass456",
      "fecha_nacimiento": "1990-12-15",
      "telefono": "123456789",
      "token": 9876543210,
      "role": 2,
      "created_by": "2022-01-01T11:00:00Z",
      "updated_by": "2022-01-01T11:00:00Z",
      "estado_user": true
    },
    {
      "id": 3,
      "nombres": "Carlos",
      "apellidos": "Rodríguez",
      "email": "carlos@example.com",
      "password": "pass789",
      "fecha_nacimiento": "1988-08-30",
      "telefono": "555555555",
      "token": 5555555555,
      "role": 3,
      "created_by": "2022-01-01T12:00:00Z",
      "updated_by": "2022-01-01T12:00:00Z",
      "estado_user": true
    }
  ]
}


-- Tabla de Institucion
CREATE TABLE `Institucion` (
  `id_institucion` int not null auto_increment,
  `nombre` VARCHAR(50) unique,
  `direccion` VARCHAR(50),
   CONSTRAINT pk_id_institucion PRIMARY KEY (id_institucion)
);

INSERT INTO Institucion (nombre, direccion) VALUES ('TECSUP', 'Av Cascanueces ');
INSERT INTO Institucion (nombre, direccion) VALUES ('Institución B', 'Dirección B');

{
  "instituciones": [
    {
      "id_institucion": 1,
      "nombre": "Institución A",
      "direccion": "Dirección A"
    },
    {
      "id_institucion": 2,
      "nombre": "Institución B",
      "direccion": "Dirección B"
    }
  ]
}




CREATE TABLE `Perfil` (
  `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `id_user` BIGINT,
  `id_institucion` INT,
  `dni` VARCHAR(8),
  `carnet_extranjeria` VARCHAR(20),
  CONSTRAINT ck_dni_or_carnet CHECK (
    (dni IS NOT NULL AND carnet_extranjeria IS NULL) OR
    (dni IS NULL AND carnet_extranjeria IS NOT NULL)),
  CONSTRAINT fk_id_user FOREIGN KEY (id_user) REFERENCES Usuarios(id),
  CONSTRAINT fk_id_institucion FOREIGN KEY (id_institucion) REFERENCES institucion(id_institucion),
  CONSTRAINT ck_dni_format CHECK (dni REGEXP '^[0-9]{8}$'),
  CONSTRAINT ck_carnet_format CHECK (carnet_extranjeria REGEXP '^[0-9]{6,12}$')
);


CREATE TABLE `Anuncio` (
  `id_anuncio` int not null auto_increment,
  `id_user` BIGINT,
  /* Propósito: alquiler por meses, estadía, por día, horas */
  `proposito` varchar(50),
  `titulo` varchar(30),
  `descripcion` varchar(100),
  `ubicacion` varchar(50),
  `precio_min` decimal(10,2) ,
  `precio_max` decimal(10,2) ,
  `tipo_espacio` varchar(30),
  `num_hab` int,
  `num_cama` int,
  `dimensiones` decimal(10,2),
  `estado_anuncio` char(1),
  constraint check_precio_max check(precio_max > precio_min),
  constraint check_precio_positivo check(precio_max > 0 AND precio_min > 0),
  CONSTRAINT pk_id_anuncio PRIMARY KEY (id_anuncio),
  CONSTRAINT fk_id_user_anuncio FOREIGN KEY (id_user) 
  REFERENCES Usuarios(id)
);


CREATE TABLE `Imagenes` (
  `id_imagen` int not null auto_increment,
  `ruta` blob, 
  CONSTRAINT pk_id_imagen PRIMARY KEY (id_imagen)
);

CREATE TABLE `Anuncio_Imagen` (
  `id` int not null auto_increment PRIMARY KEY,
  `id_anuncio` int ,
  `id_imagen` int ,
   FOREIGN KEY (id_anuncio) REFERENCES Anuncio(id_anuncio),
   FOREIGN KEY (id_imagen) REFERENCES Imagenes(id_imagen)
);

CREATE TABLE `Perfil_Imagen` (
  `id` int not null auto_increment PRIMARY KEY,
  `id_perfil` BIGINT ,
  `id_imagen` int ,
   FOREIGN KEY (id_perfil) REFERENCES Perfil(id),
   FOREIGN KEY (id_imagen) REFERENCES Imagenes(id_imagen)
);

CREATE TABLE `Etiqueta` (
  `id_etiqueta` int not null auto_increment,
  `nombre` VARCHAR(20),
  CONSTRAINT pk_id_etiqueta PRIMARY KEY (id_etiqueta)
);

CREATE TABLE `Anuncio_Etiqueta` (
  `id` int not null auto_increment PRIMARY KEY,
  `id_anuncio` int ,
  `id_etiqueta` int ,
   FOREIGN KEY (id_anuncio) REFERENCES Anuncio(id_anuncio),
   FOREIGN KEY (id_etiqueta) REFERENCES Etiqueta(id_etiqueta)
);
from django.db import models


-- class Usuarios(models.Model):
--   id = models.BigAutoField(primary_key=True)
--   nombres = models.CharField(max_length=255)
--   apellidos = models.CharField(max_length=255)
--   email = models.CharField(max_length=255, unique=True)
--   password = models.CharField(max_length=255)
--   fecha_nacimiento = models.DateField(null=True)
--   telefono = models.CharField(max_length=255)
--   token = models.BigIntegerField()
--   role = models.IntegerField()
--   created_by = models.DateTimeField(auto_now_add=True)
--   updated_by = models.DateTimeField(auto_now=True)
--   estado_user = models.BooleanField()


-- class Institucion(models.Model):
--   id_institucion = models.IntegerField(primary_key=True)
--   nombre = models.CharField(max_length=50, unique=True)
--   direccion = models.CharField(max_length=50)


-- class Perfil(models.Model):
--   id = models.BigAutoField(primary_key=True)
--   id_user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
--   id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
--   dni = models.CharField(max_length=8, null=True)
--   carnet_extranjeria = models.CharField(max_length=20, null=True)

--   class Meta:
--     constraints = [
--       models.CheckConstraint(
--         check=models.Q(dni__isnull=False, carnet_extranjeria__isnull=True) |
--             models.Q(dni__isnull=True, carnet_extranjeria__isnull=False),
--         name='ck_dni_or_carnet'
--       ),
--       models.CheckConstraint(
--         check=models.Q(dni__regex=r'^[0-9]{8}$'),
--         name='ck_dni_format'
--       ),
--       models.CheckConstraint(
--         check=models.Q(carnet_extranjeria__regex=r'^[0-9]{6,12}$'),
--         name='ck_carnet_format'
--       )
--     ]


-- class Anuncio(models.Model):
--   id_anuncio = models.IntegerField(primary_key=True)
--   id_user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
--   proposito = models.CharField(max_length=50)
--   titulo = models.CharField(max_length=30)
--   descripcion = models.CharField(max_length=100)
--   ubicacion = models.CharField(max_length=50)
--   precio_min = models.DecimalField(max_digits=10, decimal_places=2)
--   precio_max = models.DecimalField(max_digits=10, decimal_places=2)
--   tipo_espacio = models.CharField(max_length=30)
--   num_hab = models.IntegerField()
--   num_cama = models.IntegerField()
--   dimensiones = models.DecimalField(max_digits=10, decimal_places=2)
--   estado_anuncio = models.CharField(max_length=1)

--   class Meta:
--     constraints = [
--       models.CheckConstraint(
--         check=models.Q(precio_max__gt=models.F('precio_min')),
--         name='check_precio_max'
--       ),
--       models.CheckConstraint(
--         check=models.Q(precio_max__gt=0) & models.Q(precio_min__gt=0),
--         name='check_precio_positivo'
--       )
--     ]


-- class Imagenes(models.Model):
--   id_imagen = models.IntegerField(primary_key=True)
--   ruta = models.BinaryField()


-- class Anuncio_Imagen(models.Model):
--   id = models.IntegerField(primary_key=True)
--   id_anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
--   id_imagen = models.ForeignKey(Imagenes, on_delete=models.CASCADE)


-- class Perfil_Imagen(models.Model):
--   id = models.IntegerField(primary_key=True)
--   id_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
--   id_imagen = models.ForeignKey(Imagenes, on_delete=models.CASCADE)


-- class Etiqueta(models.Model):
--   id_etiqueta = models.IntegerField(primary_key=True)
--   nombre = models.CharField(max_length=20)


-- class Anuncio_Etiqueta(models.Model):
--   id = models.IntegerField(primary_key=True)
--   id_anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
--   id_etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)



