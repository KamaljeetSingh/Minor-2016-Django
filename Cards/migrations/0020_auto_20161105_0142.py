# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 20:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0019_auto_20161105_0141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cards',
            name='key',
        ),
        migrations.AddField(
            model_name='cards',
            name='id',
            field=models.AutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cards',
            name='card_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 5, 1, 41, 47, 628913)),
        ),
    ]