from rest_framework import serializers

from .models import Proudcut

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proudcut
        fields = ['id','name','description','price','stock','created_at','updated_at']

class ProductviewSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Proudcut
        fields = ['name', 'description', 'price']
class ProductcreatesSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Proudcut
        fields = ['name','description','price','stock']

class ProductupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proudcut
        fields = ['id','name','description','price','stock']

class ProductdeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proudcut
        fields = ['id']
        
