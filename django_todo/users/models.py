from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(default='if_elif_else.jpg', upload_to="users")
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(default="my address")

    def __str__(self):
        return str(self.user.username)


