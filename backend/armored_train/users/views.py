import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Level, Score
from .serializers import LevelSerializer, ScoreSerializer


class LevelListView(RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ScoreListView(RetrieveAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class AuthorizationView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=401)


class RegistrationView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.create_user(username=username, password=password)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=409)
        return JsonResponse({'success': 'User registered successfully'}, status=201)
