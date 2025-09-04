from django.shortcuts import render
from .serializers import *
from .models import Proudcut
from rest_framework import generics


class ProudcutlistView(generics.ListAPIView):
    queryset = Proudcut.objects.all()
    serializer_class = ProductSerializer

class Productcreatlist(generics.CreateAPIView):
    queryset = Proudcut.objects.all()
    serializer_class = ProductcreatesSerliazer
    

class productuserview(generics.ListAPIView):
    queryset = Proudcut.objects.all()
    serializer_class = ProductviewSerilizer

class productupdate(generics.UpdateAPIView):
    queryset = Proudcut.objects.all()
    serializer_class = ProductupdateSerializer

class productdelate(generics.DestroyAPIView):
    queryset = Proudcut.objects.all()
    serializer_class = ProductdeleteSerializer



# Create your views here.
