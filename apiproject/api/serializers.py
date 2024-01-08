
from rest_framework import serializers
from api.models import Vehicles,Category
from django.contrib.auth.models import User

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicles
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"


class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password"]      

        
