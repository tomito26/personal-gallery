# Generated by Django 3.1.2 on 2020-11-09 14:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleryApp', '0004_auto_20201011_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
    ]
