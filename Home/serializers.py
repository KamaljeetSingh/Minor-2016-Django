from rest_framework import serializers
from .models import *
from Boards.models import *


class UsersinfoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Boards
        fields = ['uuid', 'title','listInsideProjects']
        depth = 2
