from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Message(models.Model):
	name = models.CharField(max_length=20)
	text = models.TextField()
	massage_date = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return F"{self.name} {self.massage_date}"


