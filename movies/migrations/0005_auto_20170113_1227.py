# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 17:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20170112_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='owned',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='wishlist',
        ),
        migrations.AddField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('O', 'Owned'), ('W', 'Wishlist')], default='O', max_length=1),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(message='Illegal characters. Use letters only', regex='[A-Za-z]')]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]