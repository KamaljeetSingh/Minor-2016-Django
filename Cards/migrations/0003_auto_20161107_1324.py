# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-07 07:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0002_auto_20161106_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='cards',
            name='card_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 7, 13, 24, 28, 322115)),
        ),
    ]
