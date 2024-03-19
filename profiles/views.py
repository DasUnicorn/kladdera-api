from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response(users)