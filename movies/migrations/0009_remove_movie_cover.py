# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 20:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20170113_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='cover',
        ),
    ]
