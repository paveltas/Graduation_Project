from rest_framework.generics import RetrieveAPIView

from .models import Level, Score
from .serializers import LevelSerializer, ScoreSerializer


class LevelDetailView(RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ScoreDetailView(RetrieveAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
