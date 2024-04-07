from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Mood
from .serializers import MoodSerializer
from kladdera_api.permissions import IsOwner


class MoodList(APIView):
    serializer_class = MoodSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):
        moods = Mood.objects.filter(user=request.user)
        serializer = MoodSerializer(
            moods, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = MoodSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class MoodDetail(APIView):
    permission_classes = [IsAuthenticated & IsOwner]
    serializer_class = MoodSerializer

    def get_object(self, pk):
        try:
            mood = Mood.objects.get(pk=pk)
            self.check_object_permissions(self.request, mood)
            return mood
        except Mood.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mood = self.get_object(pk)
        self.check_object_permissions(request, mood)
        serializer = MoodSerializer(
            mood, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        mood = self.get_object(pk)
        self.check_object_permissions(request, mood)
        serializer = MoodSerializer(
            mood, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        mood = self.get_object(pk)
        self.check_object_permissions(request, mood)
        mood.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
