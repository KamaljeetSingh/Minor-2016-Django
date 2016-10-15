from rest_framework import serializers
from .models import *


class CardsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cards
        fields = ['id', 'database']
        depth = 2