# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-05 13:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0027_auto_20161105_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cards',
            name='k',
        ),
        migrations.AlterField(
            model_name='cards',
            name='card_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 5, 18, 56, 22, 260863)),
        ),
    ]
