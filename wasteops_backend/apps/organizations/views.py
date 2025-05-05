from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Organization, Facility, Car, WasteContainer
from .serializers import OrganizationSerializer, FacilitySerializer, CarSerializer, WasteContainerSerializer


class UserOrganizationRetrieveAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrganizationSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        organization = user.organizations.first()  # Assuming 'related_name="organizations"' in Organization model

        if organization:
            serializer = self.get_serializer(organization)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"detail": "User does not belong to any organization."},
                status=status.HTTP_404_NOT_FOUND
            )


# -- Organization Core Views --
class OrganizationCreateAPIView(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# -- Facilities Views --

# Create Facility
class FacilityCreateAPIView(generics.CreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        organization = self.request.user.organizations.first()
        if not organization:
            raise ValueError("User does not have any associated organization")
        serializer.save(organization=organization)


# Get Facility (Single)
class FacilityRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [IsAuthenticated]


# Get All Facilities
class FacilityListAPIView(generics.ListAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [IsAuthenticated]


# Delete Facility
class FacilityDestroyAPIView(generics.DestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [IsAuthenticated]

# -- Cars Views --


# Create Car
class CarCreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        organization = self.request.user.organizations.first()
        if not organization:
            raise ValueError("User does not have any associated organization")
        serializer.save(organization=organization)


# Get Car (Single)
class CarRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


# Get All Cars
class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


# Delete Car
class CarDestroyAPIView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

# -- Waste Containers Views --


# Create WasteContainer
class WasteContainerCreateAPIView(generics.CreateAPIView):
    queryset = WasteContainer.objects.all()
    serializer_class = WasteContainerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        organization = self.request.user.organizations.first()
        if not organization:
            raise ValueError("User does not have any associated organization")
        serializer.save(organization=organization)


# Get WasteContainer (Single)
class WasteContainerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = WasteContainer.objects.all()
    serializer_class = WasteContainerSerializer
    permission_classes = [IsAuthenticated]


# Get All WasteContainers
class WasteContainerListAPIView(generics.ListAPIView):
    queryset = WasteContainer.objects.all()
    serializer_class = WasteContainerSerializer
    permission_classes = [IsAuthenticated]


# Delete WasteContainer
class WasteContainerDestroyAPIView(generics.DestroyAPIView):
    queryset = WasteContainer.objects.all()
    serializer_class = WasteContainerSerializer
    permission_classes = [IsAuthenticated]
