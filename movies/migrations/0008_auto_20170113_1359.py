# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movie_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover',
            field=models.ImageField(default='No image', upload_to='cover/'),
        ),
    ]
