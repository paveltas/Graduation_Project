from rest_framework import serializers
from .models import User, Game


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'total_score']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['user', 'level1_score', 'level2_score', 'level3_score']
