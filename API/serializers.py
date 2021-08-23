from rest_framework import serializers
from mainApp.models import BuyerPostRequest, Category, Services, Offer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token




class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class OfferSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class BuyerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerPostRequest
        fields = '__all__'