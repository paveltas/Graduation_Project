from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    total_score = models.IntegerField(default=0)


class Game(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='game')
    level1_score = models.IntegerField(default=0)
    level2_score = models.IntegerField(default=0)
    level3_score = models.IntegerField(default=0)
