from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('messages/', views.message_view, name="messages"),
    path('home_view/', views.home_view, name="home_view"),
    path('register/', views.user_register, name="register"),
]
