from rest_framework import serializers
from .models import CustomUser


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'created_on', 'is_active', 'is_admin']
