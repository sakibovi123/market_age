from django.urls import path, include
from AdminPanel import views

urlpatterns = [
    path('', views.get_adminpanel_url, name="AdminHome"),
]