from django.shortcuts import render
from api.models import Vehicles
from rest_framework.views import APIView
from api.serializers import VehicleSerializer
from rest_framework.response import Response
# Create your views here.
# localhost:8000//api/vehicles/
# method:get
# method:post


class VehicleView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Vehicles.objects.all()
        # de serialization
        # here many is true because all objects are taking
        serializer=VehicleSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kwargs):
        # serialising first
        serializer=VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

# localhost:8000/api/vehicles/2/
class VehicleDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vehicles.objects.get(id=id)
        # here many is false.only one object is taking
        serializer=VehicleSerializer(qs,many=False)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Vehicles.objects.get(id=id)
        serializer=VehicleSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Vehicles.objects.get(id=id)
        obj.delete()
        return Response(data="deleted")    
                
        
 







