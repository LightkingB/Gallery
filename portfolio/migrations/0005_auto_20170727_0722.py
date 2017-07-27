# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 04:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20170726_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='category',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Category'),
            preserve_default=False,
        ),
    ]