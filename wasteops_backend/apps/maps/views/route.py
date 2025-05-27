from rest_framework import viewsets
from apps.maps.models import Route
from apps.maps.serializers.route import RouteSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def perform_create(self, serializer):
        user = self.request.user
        organization = user.organizations.first()
        serializer.save(created_by=user, organization=organization)
