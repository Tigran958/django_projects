from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Actor, Movie

import datetime
import json


# Create your views here.
def home(request):
    context = {"name": "Eric",
               "surname": "Sargsyan"
    }
    return render(request, 'first_app/home.html', context)
    # return HttpResponse("<h1>This is home page</h1>")


def actors(request):

    # actors = Actor.objects.all()
    movie = Movie.objects.all()

    data = {
            # 'items': actors,
            'movies': movie,
            }

    return render(request, "first_app/actors.html", data)
