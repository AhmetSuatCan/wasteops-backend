from rest_framework import viewsets
from apps.operations.models import Team, UserTeam
from rest_framework.permissions import IsAuthenticated
from apps.operations.serializers import TeamSerializer
from apps.users.permissions import IsAdmin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Team.objects.none()

        user = self.request.user
        organization = user.organizations.first()
        return Team.objects.filter(organization=organization,
                                   disband_date__isnull=True
                                   )

    def perform_create(self, serializer):
        user = self.request.user
        organization = user.organizations.first()
        serializer.save(organization=organization)


class DisbandTeamView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            team = Team.objects.get(pk=pk, disband_date__isnull=True)
        except Team.DoesNotExist:
            return Response({'detail': 'Team not found or already disbanded.'}, status=status.HTTP_404_NOT_FOUND)

        disband_time = timezone.now()
        team.disband_date = disband_time
        team.save()

        # Soft-remove all active members
        UserTeam.objects.filter(
            team=team,
            removed_at__isnull=True
        ).update(removed_at=disband_time)

        return Response({'detail': 'Team disbanded and members removed.'}, status=status.HTTP_200_OK)
