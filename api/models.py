from django.db import models

# Create your models here.
class GetUsers(models.Model):
    username = models.CharField(max_length=255)
    client_ip = models.TextField()
    location = models.TextField()
    greetings = models.TextField()

    def __str__(self):
        return f"{self.username}"