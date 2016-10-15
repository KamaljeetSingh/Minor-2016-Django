# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-22 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cards', '0003_auto_20160822_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardsinfo',
            name='activity',
            field=models.CharField(default=None, max_length=10000),
        ),
        migrations.AlterField(
            model_name='cardsinfo',
            name='attachment',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cardsinfo',
            name='due_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='cardsinfo',
            name='photo',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]