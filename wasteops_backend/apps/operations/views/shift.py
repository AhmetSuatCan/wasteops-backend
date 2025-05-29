from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.operations.models import ShiftModel, Team
from apps.operations.serializers.shift import ShiftSerializer
from apps.maps.models import Route
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema


class ShiftViewSet(viewsets.ModelViewSet):
    serializer_class = ShiftSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put', 'patch', 'delete', 'head', 'options']

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return ShiftModel.objects.none()
        user = self.request.user
        return ShiftModel.objects.filter(organization=user.organizations.first())

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organizations.first())


class CreateShiftView(APIView):

    @swagger_auto_schema(request_body=ShiftSerializer)
    def post(self, request):
        route_id = request.data.get("route_id")
        team_id = request.data.get("team_id")
        start_time = request.data.get("start_time", timezone.now())
        name = request.data.get("name", "Unnamed Shift")

        if not route_id or not team_id:
            return Response({"detail": "route_id and team_id are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            route = Route.objects.get(id=route_id)
            team = Team.objects.get(id=team_id)
        except (Route.DoesNotExist, Team.DoesNotExist):
            return Response({"detail": "Invalid route_id or team_id."}, status=status.HTTP_404_NOT_FOUND)

        organization = request.user.organizations.first()

        shift = ShiftModel.objects.create(
            name=name,
            route=route,
            team=team,
            start_time=start_time,
            organization=organization
        )

        return Response(ShiftSerializer(shift).data, status=status.HTTP_201_CREATED)


class UpdateShiftEndTimeView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, shift_id):
        try:
            shift = ShiftModel.objects.get(id=shift_id)
        except ShiftModel.DoesNotExist:
            return Response({'detail': 'Shift not found.'}, status=status.HTTP_404_NOT_FOUND)

        end_time = request.data.get("end_time", timezone.now())
        shift.end_time = end_time
        shift.save()

        return Response({'detail': 'Shift end_time updated successfully.', 'end_time': shift.end_time}, status=status.HTTP_200_OK)
