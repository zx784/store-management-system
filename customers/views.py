from django.shortcuts import render
from .serializers import*
from .models import *
from rest_framework import generics
from .permissions import *

class CustomerRegistrtion(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerrRegisterSerializer
    
class Updataprofile(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerrRegisterSerializer

class ListAllusers(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = coustomerserlaiaer
    permission_classes = [IsAdmin]
class Deleteaccount(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = coustomerdeleteaccount
    permission_classes = [IsAdminOrUser]