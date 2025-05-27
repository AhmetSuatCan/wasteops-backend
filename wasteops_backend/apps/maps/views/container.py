# views/container.py
from rest_framework import viewsets
from apps.maps.models import Container
from apps.maps.serializers import ContainerSerializer


class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
