from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class Team(models.Model):
#   team_name = models.CharField(max_length=255, unique=True)

#   def __str__(self):
#     return self.team_name
  
# class CustomUser(AbstractUser):
# #   team = models.ForeignKey(Team, on_delete=models.CASCADE)

#   def __str__(self):
#     return self.username


class Team(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self) :
        return self.name

class User(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self) :
        return self.username