from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Organization, Facility, Car, WasteContainer
from .serializers import (
    OrganizationSerializer,
    FacilitySerializer,
    CarSerializer,
    WasteContainerSerializer,
)

# Mixin to automatically assign the user's organization
class AutoOrganizationMixin:
    def perform_create(self, serializer):
        organization = self.request.user.organizations.first()
        if not organization:
            raise ValueError("User does not belong to any organization.")
        serializer.save(organization=organization)


# -- Organization ViewSet --
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=["get"], url_path="check-owned-organization")
    def my_organization(self, request):
        organization = request.user.organizations.first()
        if organization:
            serializer = self.get_serializer(organization)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "User does not belong to any organization."},
            status=status.HTTP_404_NOT_FOUND,
        )


# -- Facility ViewSet --
class FacilityViewSet(AutoOrganizationMixin, viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [IsAuthenticated]


# -- Car ViewSet --
class CarViewSet(AutoOrganizationMixin, viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


# -- Waste Container ViewSet --
class WasteContainerViewSet(AutoOrganizationMixin, viewsets.ModelViewSet):
    queryset = WasteContainer.objects.all()
    serializer_class = WasteContainerSerializer
    permission_classes = [IsAuthenticated]
