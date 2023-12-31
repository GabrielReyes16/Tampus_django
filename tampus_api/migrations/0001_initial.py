# Generated by Django 4.2.7 on 2023-12-05 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id_anuncio', models.BigAutoField(primary_key=True, serialize=False)),
                ('proposito', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=50)),
                ('precio_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_max', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_espacio', models.CharField(max_length=30)),
                ('num_hab', models.IntegerField()),
                ('num_cama', models.IntegerField()),
                ('dimensiones', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado_anuncio', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id_etiqueta', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id_imagen', models.IntegerField(primary_key=True, serialize=False)),
                ('ruta', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id_institucion', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=8, null=True)),
                ('carnet_extranjeria', models.CharField(max_length=20, null=True)),
                ('id_institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tampus_api.institucion')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('telefono', models.CharField(max_length=255)),
                ('token', models.BigIntegerField()),
                ('role', models.IntegerField()),
                ('created_by', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.DateTimeField(auto_now=True)),
                ('estado_user', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Perfil_Imagen',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('id_imagen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tampus_api.imagenes')),
                ('id_perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tampus_api.perfil')),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tampus_api.usuarios'),
        ),
        migrations.CreateModel(
            name='Anuncio_Imagen',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('id_anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tampus_api.anuncio')),
                ('id_imagen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tampus_api.imagenes')),
            ],
        ),
        migrations.CreateModel(
            name='Anuncio_Etiqueta',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('id_anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tampus_api.anuncio')),
                ('id_etiqueta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tampus_api.etiqueta')),
            ],
        ),
        migrations.AddField(
            model_name='anuncio',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tampus_api.usuarios'),
        ),
        migrations.AddConstraint(
            model_name='perfil',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('carnet_extranjeria__isnull', True), ('dni__isnull', False)), models.Q(('carnet_extranjeria__isnull', False), ('dni__isnull', True)), _connector='OR'), name='ck_dni_or_carnet'),
        ),
        migrations.AddConstraint(
            model_name='perfil',
            constraint=models.CheckConstraint(check=models.Q(('dni__regex', '^[0-9]{8}$')), name='ck_dni_format'),
        ),
        migrations.AddConstraint(
            model_name='perfil',
            constraint=models.CheckConstraint(check=models.Q(('carnet_extranjeria__regex', '^[0-9]{6,12}$')), name='ck_carnet_format'),
        ),
        migrations.AddConstraint(
            model_name='anuncio',
            constraint=models.CheckConstraint(check=models.Q(('precio_max__gt', models.F('precio_min'))), name='check_precio_max'),
        ),
        migrations.AddConstraint(
            model_name='anuncio',
            constraint=models.CheckConstraint(check=models.Q(('precio_max__gt', 0), ('precio_min__gt', 0)), name='check_precio_positivo'),
        ),
    ]
