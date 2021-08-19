from django.urls import path
from django.conf.urls.static import static
from django.conf.urls.static import static
from .views import ServiceApiView, GigApiView


urlpatterns = [
    path('services/', ServiceApiView.as_view()),
    path('gigs/', GigApiView.as_view()),
]
