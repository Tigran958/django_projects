from django.urls import path
from .views import home, last_name

urlpatterns = [
    path('home/', home, name="home" ),   
    path('name_last/', last_name, name="last_name" ),   
]