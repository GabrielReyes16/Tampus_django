# Generated by Django 4.0.1 on 2023-12-12 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tampus_api', '0003_anuncioetiqueta_favoritos_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anuncio',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='etiqueta',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='usuarios',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='estado_anuncio',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tampus_api.usuarios'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='proposito',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='tipo_espacio',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='titulo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterModelTable(
            name='anuncio',
            table='anuncio',
        ),
        migrations.AlterModelTable(
            name='anuncioetiqueta',
            table='anuncio_etiqueta',
        ),
        migrations.AlterModelTable(
            name='etiqueta',
            table='etiqueta',
        ),
        migrations.AlterModelTable(
            name='favoritos',
            table='favoritos',
        ),
        migrations.AlterModelTable(
            name='usuarios',
            table='usuarios',
        ),
    ]
