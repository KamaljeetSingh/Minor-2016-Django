# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-17 14:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0011_auto_20160824_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='card_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 17, 20, 8, 54, 307442)),
        ),
    ]