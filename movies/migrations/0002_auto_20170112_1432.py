# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 19:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('movie_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='movies.Movie')),
                ('date_added', models.DateField(verbose_name='Added on')),
            ],
            bases=('movies.movie',),
        ),
        migrations.AlterField(
            model_name='owned',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(5, 'Great'), (4, 'Good'), (3, 'Okay'), (2, 'Bad'), (1, 'Awful')]),
        ),
    ]
