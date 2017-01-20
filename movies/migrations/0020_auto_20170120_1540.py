# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0019_auto_20170120_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('act', 'Action'), ('com', 'Comedy'), ('dra', 'Drama'), ('fan', 'Fantasy'), ('hor', 'Horror'), ('sci', 'Science Fiction'), ('doc', 'Documentary'), ('rom', 'Romance'), ('unk', 'Unknown')], default='unk', max_length=3),
        ),
    ]
