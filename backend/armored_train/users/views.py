import json

from django.contrib.auth.models import User
from django.db.models import Sum, F, Window
from django.db.models.functions import DenseRank
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Score
from .serializers import ScoreSerializer


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


def rating_view(request):
    # Получение логина залогиненного пользователя
    user = request.user
    user_score = Score.objects.filter(player=user)
    print(f'user_score {user_score}')

    # Получение общего количества очков залогиненного пользователя по всем уровням
    total_points = user_score.aggregate(total_points=Sum('points'))
    print(f'total_points {total_points}')

    users_scores = (
        Score.objects
        .values('player')
        .annotate(total_points=Sum('points'))
    )
    print(f"users_score {users_scores}")

    # Получение места залогиненного пользователя среди всех остальных пользователей

    user_place = sum(1 for el in users_scores if el['total_points'] > total_points['total_points']) + 1

    # Получение данных всех пользователей

    all_users_scores = (
        Score.objects
        .annotate(player_username=F('player__username'))
        .annotate(total_points=Sum('player__score__points'))
        .order_by('-total_points')
        .annotate(place=Window(expression=DenseRank(), order_by=F('total_points').desc()))
        .values('player_username', 'total_points', 'place')
    )

    users_overall_score = [(el['place'], el['player_username'], el['total_points']) for el in all_users_scores]

    print(f'json.dumps {json.dumps(users_overall_score)}')

    print(f'users_overall_score {users_overall_score}')
    # по каждому уровню
    # all_users_scores = (
    #     Score.objects
    #     .annotate(player_username=F('player__username'))
    #     .annotate(total_points=Sum('points'))
    #     .order_by('-total_points')
    #     .annotate(place=Window(expression=DenseRank(), order_by=F('total_points').desc()))
    #     .values('player_username', 'total_points', 'place')
    # )

    # return render(request, 'test.html',
    #               {'user_score': user_score,
    #                'user_login': user.username,
    #                'total_points': total_points['total_points'],
    #                'user_place': user_place,
    #                'all_users_scores': all_users_scores}
    #               )

    return json.dumps(users_overall_score)
