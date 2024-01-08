from django.contrib.auth.models import User
from api.models import Category,Vehicles,VehiclePics,WishList

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Category  # Specify the actual model here
        fields = '__all__'  


class VehiclePicSerializer(serializers.ModelSerializer):    
    class Meta:
        model=VehiclePics
        fields=["image"]

   
class VehicleSerializer(serializers.ModelSerializer):
    owner=serializers.CharField(read_only=True)
    category=serializers.CharField(read_only=True)
    vehicle_image=VehiclePicSerializer(many=True)
    class Meta:
        model=Vehicles
        fields="__all__"

    def create(self,validated_data):
        print(validated_data)  
        return super().create(validated_data) 



class WishListSerializers(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    vehicle=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta:
        model=WishList
        fields=["user","vehicle","date"]
