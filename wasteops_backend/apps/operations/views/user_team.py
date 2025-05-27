from rest_framework import viewsets, permissions
from django.db.models import Q, Count, F
from apps.operations.models import UserTeam
from apps.operations.serializers import UserTeamSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.human_resources.models import Employment
from apps.human_resources.serializers import EmploymentMiniSerializer
from rest_framework import status
from django.utils import timezone


class UserTeamViewSet(viewsets.ModelViewSet):
    queryset = UserTeam.objects.all()
    serializer_class = UserTeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        if getattr(self, 'swagger_fake_view', False):
            return UserTeam.objects.none()

        return UserTeam.objects.filter(
            employment__organization=self.request.user.organizations.first()
        )


class UnteamedEmployeesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        organization = request.user.organizations.first()
        unteamed_employments = Employment.objects.filter(
            organization=organization,
            end_date__isnull=True
        ).annotate(
            active_team_count=Count('team_memberships', filter=Q(team_memberships__removed_at__isnull=True))
        ).filter(
            active_team_count=0
        )
        data = EmploymentMiniSerializer(unteamed_employments, many=True).data
        return Response(data)


class TeamMembersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, team_id):
        members = UserTeam.objects.filter(
            team_id=team_id,
            removed_at__isnull=True
        ).select_related('employment__user')

        serializer = UserTeamSerializer(members, many=True)
        return Response(serializer.data)

class SoftRemoveUserTeamView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            user_team = UserTeam.objects.get(pk=pk, removed_at__isnull=True)
        except UserTeam.DoesNotExist:
            return Response({'detail': 'Active team assignment not found.'}, status=status.HTTP_404_NOT_FOUND)

        user_team.removed_at = timezone.now()
        user_team.save()

        return Response({'detail': 'User removed from team.'}, status=status.HTTP_200_OK)
