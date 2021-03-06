# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_auto_20170117_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, choices=[('act', 'Action'), ('com', 'Comedy'), ('dra', 'Drama'), ('fan', 'Fantasy'), ('hor', 'Horror'), ('sci', 'Science Fiction'), ('doc', 'Documentary')], max_length=3),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('O', 'Owned'), ('W', 'Wishlist')], default='O', max_length=1),
        ),
    ]
