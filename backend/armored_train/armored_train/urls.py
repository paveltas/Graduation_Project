from django.contrib import admin
from django.urls import path

from users.views import LevelListView, ScoreListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('level/<int:pk>/', LevelListView.as_view(), name='level-detail'),
    path('score/<int:pk>/', ScoreListView.as_view(), name='score-detail'),
]
