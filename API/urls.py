from django.urls import path
from django.conf.urls.static import static
from django.conf.urls.static import static
from .views import BuyerPostRequestView, CategoryInterestedView, CategoryView, ServiceApiView, OfferApiView


urlpatterns = [
    path('services/', ServiceApiView.as_view()),
    path('offers/', OfferApiView.as_view()),
    path('category/', CategoryView.as_view()),
    path('interested_category/', CategoryInterestedView.as_view()),
    path('buyer_posts/', BuyerPostRequestView.as_view()),
]
