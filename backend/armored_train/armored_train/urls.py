from django.contrib import admin
from django.urls import path
from djoser.views import TokenCreateView, TokenDestroyView

from users.views import AuthorizationView, RegistrationView, OverallScoreListView, rating_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('score/', OverallScoreListView.as_view(), name='overall-score-detail'),
    path('auth/token/create/', TokenCreateView.as_view(), name='token_create'),
    path('auth/token/destroy/', TokenDestroyView.as_view(), name='token_destroy'),
    path('auth/token/authorize/', AuthorizationView.as_view(), name='token_authorize'),
    path('auth/register/', RegistrationView.as_view(), name='register_user'),
    path('1/', rating_view, name='register_user'),
]
