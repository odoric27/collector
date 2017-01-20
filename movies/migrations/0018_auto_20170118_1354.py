# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 18:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_auto_20170118_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(message='Illegal characters. Use letters only', regex='[A-Za-z]')]),
        ),
        migrations.DeleteModel(
            name='Director',
        ),
    ]