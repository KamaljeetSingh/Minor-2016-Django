from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
import uuid

# Create your models here.
'''
title = 0
desc = 6
comment = 1
image = 2
checklist = 3
audionote = 4
file = 5
'''


class Checklist(models.Model):
    title = models.CharField(max_length=500)
    #list_date = models.DateField(default=datetime.now())

    def __str__(self):
        return str(self.title)


class ChecklistItems(models.Model):
    item = models.CharField(max_length=500)
    Check_title = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.item + '-' + str(self.Check_title)


class CardsAttach(models.Model):
    photo = models.FileField(null=True)
    attachment = models.FileField(null=True)

    def __str__(self):
        return str(self.id)


class Data(models.Model):
    type = models.IntegerField()
    data = models.CharField(max_length=1000)
    checklist = models.ManyToManyField(ChecklistItems, related_name='checklist')

    def __str__(self):
        return self.data


class Cards(models.Model):
    database = models.ManyToManyField(Data, related_name='databs')
    card_date = models.DateField(default=datetime.now())
    key = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk)


'''class Boards(models.Model):
    cards_data = models.ManyToManyField(Cards, related_name='cards_data')
    board_date = models.DateField(default=datetime.now())

    def __str__(self):
        return str(self.pk)'''
