from rest_framework import serializers
from .models import *

class MasterDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Master
        fields="__all__"

class ManagerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields="__all__"
    def validate(self, attrs):
        token=self.context.get('token')
        attrs['token'] = token 
        return attrs
        