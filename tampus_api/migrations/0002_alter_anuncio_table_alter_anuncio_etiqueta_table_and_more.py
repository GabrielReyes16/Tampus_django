# Generated by Django 4.2.7 on 2023-12-05 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tampus_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='anuncio',
            table='Anuncio',
        ),
        migrations.AlterModelTable(
            name='anuncio_etiqueta',
            table='Anuncio_Etiqueta',
        ),
        migrations.AlterModelTable(
            name='anuncio_imagen',
            table='Anuncio_Imagen',
        ),
        migrations.AlterModelTable(
            name='etiqueta',
            table='Etiqueta',
        ),
        migrations.AlterModelTable(
            name='imagenes',
            table='Imagenes',
        ),
        migrations.AlterModelTable(
            name='institucion',
            table='Institucion',
        ),
        migrations.AlterModelTable(
            name='perfil',
            table='Perfil',
        ),
        migrations.AlterModelTable(
            name='perfil_imagen',
            table='Perfil_Imagen',
        ),
        migrations.AlterModelTable(
            name='usuarios',
            table='Usuarios',
        ),
    ]
