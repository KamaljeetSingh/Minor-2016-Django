# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 20:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0016_auto_20161104_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cards',
            name='id',
        ),
        migrations.AddField(
            model_name='cards',
            name='key',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cards',
            name='card_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 5, 1, 35, 58, 906328)),
        ),
    ]