from django.contrib import admin
from django.urls import path
from djoser.views import TokenCreateView, TokenDestroyView

from users.views import LevelListView, ScoreListView, AuthorizationView, RegistrationView, OverallScoreListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('level/<int:pk>/', LevelListView.as_view(), name='level-detail'),
    path('score/<int:pk>/', ScoreListView.as_view(), name='score-detail'),
    path('score/', OverallScoreListView.as_view(), name='overall-score-detail'),
    path('auth/token/create/', TokenCreateView.as_view(), name='token_create'),
    path('auth/token/destroy/', TokenDestroyView.as_view(), name='token_destroy'),
    path('auth/token/authorize/', AuthorizationView.as_view(), name='token_authorize'),
    path('auth/register/', RegistrationView.as_view(), name='register_user'),
]
