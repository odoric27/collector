# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20170112_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owned',
            name='movie_ptr',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='movie_ptr',
        ),
        migrations.AddField(
            model_name='movie',
            name='owned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='wishlist',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Owned',
        ),
        migrations.DeleteModel(
            name='WishList',
        ),
    ]
