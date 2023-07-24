from django.urls import path
from .views import UserDetailView, GameDetailView

urlpatterns = [
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
]
