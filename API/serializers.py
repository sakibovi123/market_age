from rest_framework import serializers
from mainApp.models import Services, Gig



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class GigSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = '__all__'
