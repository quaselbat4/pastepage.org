# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-24 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0013_auto_20180324_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshot',
            name='internetarchive_meta_url',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
