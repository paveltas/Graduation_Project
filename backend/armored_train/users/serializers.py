from rest_framework import serializers

from .models import Level, Score


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):
    player_name = serializers.CharField(source='player.username', read_only=True)

    class Meta:
        model = Score
        fields = ['player_name', 'level', 'points']
