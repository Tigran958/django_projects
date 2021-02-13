from django.db import models

# Create your models here.


class Actor(models.Model):

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    description = models.TextField()
    age = models.IntegerField()
    married = models.BooleanField(default=False)


    def __str__(self):
        return F"{self.name}-{self.surname}"


GENRE_CHOICES = (
                (0, "Action"),
                (1, "Drama"),
                (2, "Fantasy"),
                )


class Genre(models.Model):
    name = models.IntegerField(choices=GENRE_CHOICES)
    description = models.TextField()

    def __str__(self):
        return F"{GENRE_CHOICES[self.name][1]}"

class Movie(models.Model):

    name = models.CharField(max_length=20)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE) # object from Genre class
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return F"{self.name}-{self.genre}"
