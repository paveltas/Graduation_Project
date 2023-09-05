import json

from django.contrib.auth.models import User
from django.db.models import Sum, F, Window
from django.db.models.functions import DenseRank
from django.http import JsonResponse, HttpResponse
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


# class AuthorizationView(TokenCreateView):
#     pass


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


class RatingView(APIView):
    def get(self, request):
        user = request.user
        # if not isinstance(user, int):
        #     print(user, type(user))
        #     user = 2
        print(user)
        user_score = Score.objects.filter(player=user)

        total_points = user_score.aggregate(total_points=Sum('points'))
        print(total_points['total_points'])

        users_scores = (
            Score.objects
            .values('player')
            .annotate(total_points=Sum('points'))
        )

        user_place = sum(1 for el in users_scores if el['total_points'] > total_points['total_points']) + 1

        all_users_scores = (
            Score.objects
            .annotate(player_username=F('player__username'))
            .annotate(total_points=Sum('player__score__points'))
            .order_by('-total_points')
            .annotate(place=Window(expression=DenseRank(), order_by=F('total_points').desc()))
            .values('player_username', 'total_points', 'place')
            .distinct()
        )

        results = list(all_users_scores)
        json_data = json.dumps(results)

        # return render(request, 'test.html',
        #               {'user_score': user_score,
        #                'user_login': user.username,
        #                'total_points': total_points['total_points'],
        #                'user_place': user_place,
        #                'all_users_scores': all_users_scores}
        #               )

        try:
            json.loads(json_data)
            print("Данные являются валидным JSON. в view")
            return HttpResponse(json_data, content_type="application/json")
        except json.JSONDecodeError as e:
            print("Данные не являются валидным JSON.")
            print(f"Ошибка: {e}")

        # по каждому уровню
        # all_users_scores = (
        #     Score.objects
        #     .annotate(player_username=F('player__username'))
        #     .annotate(total_points=Sum('points'))
        #     .order_by('-total_points')
        #     .annotate(place=Window(expression=DenseRank(), order_by=F('total_points').desc()))
        #     .values('player_username', 'total_points', 'place')
        # )
