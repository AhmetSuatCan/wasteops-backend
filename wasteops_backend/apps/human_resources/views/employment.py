# apps.human_resources.views.py

from rest_framework import generics, permissions
from .serializers import GenerateJoinCodeSerializer, UseJoinCodeSerializer


class GenerateJoinCodeView(generics.CreateAPIView):
    serializer_class = GenerateJoinCodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class UseJoinCodeView(generics.CreateAPIView):
    serializer_class = UseJoinCodeSerializer
    permission_classes = [permissions.IsAuthenticated]
