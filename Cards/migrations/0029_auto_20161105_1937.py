# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-05 14:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0028_auto_20161105_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='key',
            field=models.CharField(default=datetime.datetime(2016, 11, 5, 14, 7, 49, 227634, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cards',
            name='card_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 5, 19, 37, 3, 68046)),
        ),
    ]