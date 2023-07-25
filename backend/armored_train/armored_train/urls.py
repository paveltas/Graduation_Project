from django.contrib import admin
from django.urls import path

from users.views import LevelDetailView, ScoreDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('level/<int:pk>/', LevelDetailView.as_view(), name='level-detail'),
    path('score/<int:pk>/', ScoreDetailView.as_view(), name='score-detail'),
]
