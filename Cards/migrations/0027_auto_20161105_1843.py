# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-05 13:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0026_auto_20161105_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='k',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='cards',
            name='card_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 5, 18, 43, 18, 482609)),
        ),
    ]
