from app.models import *
from rest_framework import serializers
from app.models import *

class SchoolModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        #fields='__all__'
        fields=['scname']