# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 20:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0017_auto_20161105_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cards',
            name='card_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 5, 1, 39, 42, 31943)),
        ),
        migrations.AlterField(
            model_name='cards',
            name='key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]