from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import ProfileSerializer


class UserListView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data)
