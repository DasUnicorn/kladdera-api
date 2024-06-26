from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Task
        fields = '__all__'
