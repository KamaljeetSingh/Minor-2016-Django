# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-05 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boards',
            name='shared',
            field=models.IntegerField(default=0),
        ),
    ]