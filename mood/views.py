from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Mood
from .serializers import MoodSerializer
from kladdera_api.permissions import IsSuperUserOrSelf


class MoodList(APIView):
    serializer_class = MoodSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        moods = Mood.objects.filter(user=request.user)
        print("user", request.user)
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
    permission_classes = [IsSuperUserOrSelf]
    serializer_class = MoodSerializer

    def get_object(self, pk):
        try:
            task = Mood.objects.get(pk=pk)
            self.check_object_permissions(self.request, task)
            return task
        except Mood.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = MoodSerializer(
            task, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = MoodSerializer(
            task, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
