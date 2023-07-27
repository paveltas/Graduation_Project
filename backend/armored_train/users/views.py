from rest_framework.generics import RetrieveAPIView

from .models import Level, Score
from .serializers import LevelSerializer, ScoreSerializer


class LevelListView(RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ScoreListView(RetrieveAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
