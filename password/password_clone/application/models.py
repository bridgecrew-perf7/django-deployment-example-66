from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    job = models.TextField(blank=True)
    
    country = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
