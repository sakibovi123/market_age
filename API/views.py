from API.serializers import ServiceSerializer
from mainApp.models import Services
from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mainApp.models import *
from .serializers import *


class ServiceApiView(APIView):
    def get(self, request):
        services = Services.objects.all()
        data = []
        serializer = ServiceSerializer(services, many=True)

        return Response(serializer.data)


class GigApiView(APIView):
    def get(self, request):
        gigs = Gig.objects.all()

        data = []

        serializer = GigSeriaLizer(gigs, many=True)

        return Response(serializer.data)