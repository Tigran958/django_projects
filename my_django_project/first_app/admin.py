from django.contrib import admin
from .models import Actor, Movie, Genre

# Register your models here.


admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Genre)
