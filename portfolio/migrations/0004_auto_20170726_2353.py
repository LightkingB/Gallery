# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20170726_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='slider',
            field=models.ManyToManyField(blank=True, to='portfolio.Slider'),
        ),
    ]
