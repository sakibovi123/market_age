from django.urls import path, include
from ChatApp import views


urlpatterns = [
    path("all_users/", views.get_all_users, name="AllUsers"),
    path("view_profile/<int:id>/", views.user_details, name="user_details"),
    # path("form_validation/", views.form_validation, name="form_validation"),
    path("room/", views.room, name="room"),
    path("chatting/<int:id>", views.continue_chat, name="continueChat")
]
