from django.contrib import admin
from django.urls import path
from djoser.views import TokenCreateView, TokenDestroyView

from users.views import AuthorizationView, RegistrationView, OverallScoreListView, UsersOverallScoreView, \
    UserOverallScoreView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('score/', OverallScoreListView.as_view(), name='overall-score-detail'),
    path('auth/token/create/', TokenCreateView.as_view(), name='token_create'),
    path('auth/token/destroy/', TokenDestroyView.as_view(), name='token_destroy'),
    path('auth/token/authorize/', AuthorizationView.as_view(), name='token_authorize'),
    path('auth/register/', RegistrationView.as_view(), name='register_user'),
    path('users_rating/', UsersOverallScoreView.as_view(), name='users_rating_view'),
    path('user_rating/', UserOverallScoreView.as_view(), name='user_rating_view'),
]
