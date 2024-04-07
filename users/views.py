from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from .models import CustomUser
from .serializers import CustomUserSerializer
from kladdera_api.permissions import IsSuperUserOrSelf


class CreateUserView(CreateAPIView):

    model = CustomUser
    permission_classes = [
        # Or anon users can't register
        permissions.AllowAny
    ]
    serializer_class = CustomUserSerializer
