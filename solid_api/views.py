from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import *
from . import models
from . import serializers

@api_view(['GET'])
def drinks(request):
    data = models.drinks.objects.all().values()
    serial = serializers.drinkserializers(data,many=True)
    return Response(serial.data)

@api_view(['POST'])
def addDrinks(request):
    if request.method == 'POST':
        serial = serializers.drinkserializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response(serial.errors)
    return Response({
        "error":"Not allowed"
    },status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET','PUT','DELETE'])
def changeDrinks(request,id):
    try:
        data = models.drinks.objects.get(id=id)
    except:
        return Response({
            'error':'Not found'
        },status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = serializers.drinkserializers(data)
        return Response(serial.data)
    
    if request.method == 'DELETE':
        data.delete()
        return Response({
            "delete":True
        })

    if request.method == "PUT":
        serial = serializers.drinkserializers(data,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors)

