from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from .models import CustomUser
from .serializers import CustomUserSerializer


class CreateUserView(CreateAPIView):

    model = CustomUser
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CustomUserSerializer
