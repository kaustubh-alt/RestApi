from rest_framework import serializers
from .models import Todo

class doserial(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['updated_on']

class addserial(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title','desc','cheek']
