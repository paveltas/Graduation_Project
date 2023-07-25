from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint


class Level(models.Model):
    name = models.CharField(max_length=255)


class Score(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    class Meta:
        constraints = [
            UniqueConstraint(
                'player',
                'level',
                name='user_level_score',
            ),
        ]
