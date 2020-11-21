from django.db import models

# Create your models here.

STATUS_CHOICE = (
    (0, "New"),
    (1, "Doing"),
    (2, "Done"),
)


class NewTask(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

