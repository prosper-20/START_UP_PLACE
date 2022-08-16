from django.urls import path
from .views import home, register
from django.contrib.auth import views

urlpatterns = [
    path("", home, name="home"),
    path('register/', register, name="register")
]