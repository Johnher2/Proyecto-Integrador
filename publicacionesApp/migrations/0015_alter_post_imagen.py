# Generated by Django 4.0.1 on 2022-04-23 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacionesApp', '0014_delete_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='', verbose_name='Imagen de post'),
        ),
    ]
