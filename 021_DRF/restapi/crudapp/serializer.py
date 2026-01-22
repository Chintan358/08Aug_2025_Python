from rest_framework import serializers
from crudapp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        # fields=["name","email"]
        fields="__all__"
        #exclude=['age']

