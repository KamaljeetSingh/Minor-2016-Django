# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-07 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cards', '0004_auto_20161107_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ListofCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=100)),
                ('listofcards', models.ManyToManyField(related_name='listcards', to='Cards.Card_id')),
            ],
        ),
        migrations.AddField(
            model_name='boards',
            name='listInsideProjects',
            field=models.ManyToManyField(related_name='listinside', to='Boards.ListofCards'),
        ),
    ]
