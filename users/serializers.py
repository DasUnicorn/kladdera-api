from rest_framework import serializers
from .models import CustomUser
from dj_rest_auth.models import TokenModel


class CustomUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """
    user = CustomUserSerializer(many=False, read_only=True)
    
    class Meta:
        model = TokenModel
        fields = ('key', 'user')
