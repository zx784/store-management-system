from .models import *
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

# Serializer for registering a new user
class CustomerrRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password] )
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password', 'role']
        
    def validate(self, data):
        if data['username'] == data['password']:
            raise serializers.ValidationError("The username and password cannot be the same.")
        return data
    def create(self, validated_data):
        customer = Customer.objects.create(
            username = validated_data['username'],
            email=validated_data.get('email'),
            role=validated_data['role']
        )
        # Set the password the safe way (hashing it)
        customer.set_password(validated_data['password'])
        customer.save()
        return customer
    
class coustomerserlaiaer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email']

class coustomerdeleteaccount(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'password']
        
