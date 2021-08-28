from django.urls import path, include
from AdminPanel import views

urlpatterns = [
    path('', views.get_adminpanel_url, name="AdminHome"),
    path("uploaded-offer/", views.uploadedOfferView, name="uploaded-offer"),
    path("all-users/", views.allUsersView, name="all-users"),
    path("all-orders/", views.allOrdersView, name="all-orders"),
    path("admin-login/", views.adminLoginView, name="admin-login"),
]