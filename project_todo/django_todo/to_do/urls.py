from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('task_update/<str:pk>', views.task_update, name="task_update" ),
]