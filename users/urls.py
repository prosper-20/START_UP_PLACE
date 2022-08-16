from operator import imod
from django.urls import path
from .views import home, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path('register/', register, name="register")
    path("login/", auth_view.LoginView)

]