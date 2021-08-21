from rest_framework.serializers import Serializer
from API.serializers import ServiceSerializer
from mainApp.models import Services
from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mainApp.models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ServiceApiView(APIView):
    def get(self, request):
        services = Services.objects.all()
        data = []
        serializer = ServiceSerializer(services, many=True)

        return Response(serializer.data)


class GigApiView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def get(self, request):
        gigs = Gig.objects.all()

        data = []

        serializer = GigSeriaLizer(gigs, many=True)

        user = request.user

        for gigs in serializer.data:
            favorite_gig = GigFavoriteModel.objects.filter(user=user).filter(
                gig_id=gigs['id']
            )

            if favorite_gig:
                gigs['gigfavoritemodel'] = favorite_gig[0].is_Favorite
            else:
                gigs['gigfavoritemodel'] = False
            data.append(gigs)

        return Response(serializer.data)


class GigFavoriteView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        data = request.data['id']

        try:
            gig_obj = Gig.objects.get(id=data)

            user = request.user

            single_interested_gig = GigFavoriteModel.objects.filter(user=user).filter(
                gig=gig_obj
            )

            if single_interested_gig:
                print(single_interested_gig)
                var = single_interested_gig.is_interested
                single_interested_gig.is_interested = not var
                single_interested_gig.save()
            else:
                GigFavoriteModel.objects.create(
                    gig=gig_obj, user=user, is_Favorite=True
                )

            respose_msg = {'error': False}

        except:
            response_msg = {'error': True}

        return Response(response_msg)


class CategoryView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def get(self, request):
        category = Category.objects.all()

        data = []

        serializer = CategorySerializer(category, many=True)
        user = request.user
        for category in serializer.data:
            interested_query = CategoryInterestedModel.objects.filter(user=user).filter(
                category_id=category['id']
            )

            if interested_query:
                category['categoryinterestedmodel'] = interested_query[0].is_interested
            else:
                category['categoryinterestedmodel'] = False
            data.append(category)

        return Response(serializer.data)


class CategoryInterestedView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        data = request.data['id']

        try:
            category_obj = Category.objects.get(id=data)
            user = request.user
            single_interested_category = CategoryInterestedModel.objects.filter(
                user=user
            ).filter(category=category_obj).first()

            if single_interested_category:
                print("single_iterested_category")
                var = single_interested_category.is_interested
                single_interested_category.is_interested = not var
                single_interested_category.save()
            else:
                CategoryInterestedModel.objects.create(
                    category=category_obj, user=user, is_interested=True
                )

            respose_msg = {'error': False}
        except:
            response_msg = {'error': True}

        return Response(response_msg)



class BuyerPostRequestView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    def get(self, request):
        data = []
        buyer_post = BuyerPostRequest.objects.all()
        
        serializer = BuyerPostSerializer(buyer_post, many=True)
        
        return Response(serializer.data)