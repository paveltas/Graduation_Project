import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Level, Score
from .serializers import LevelSerializer, ScoreSerializer


class OverallScoreListView(APIView):
    @staticmethod
    def get(request):
        try:
            score = Score.objects.all()
            serializer = ScoreSerializer(score, many=True)
            return Response(serializer.data)
        except Score.DoesNotExist:
            return Response({'error': 'Score does not exist'}, status=404)


class AuthorizationView(APIView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=401)


class RegistrationView(APIView):
    @staticmethod
    def post(request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.create_user(username=username, password=password)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=409)
        return JsonResponse({'success': 'User registered successfully'}, status=201)
