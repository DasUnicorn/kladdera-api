from rest_framework import serializers
from .models import Mood


class MoodSerializer(serializers.ModelSerializer):

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Mood
        fields = ['id', 'date', 'mood', 'user', 'note']
