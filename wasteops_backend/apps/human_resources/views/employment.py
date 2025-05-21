# apps.human_resources.views.py

from rest_framework import generics, permissions, status
from apps.human_resources.serializers import GenerateJoinCodeSerializer, UseJoinCodeSerializer, OrganizationJoinCodeListSerializer
from rest_framework.views import APIView
from apps.human_resources.models import OrganizationJoinCode
from rest_framework.response import Response
from apps.human_resources.models import Employment
from rest_framework.permissions import IsAuthenticated
from apps.organizations.serializers import OrganizationSerializer

'''
These two views is for generating a joining code to create an Employment.

An employment is basically a connection between a User and Organization.
'''


class GenerateJoinCodeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = GenerateJoinCodeSerializer(data={}, context={'request': request})
        serializer.is_valid(raise_exception=True)
        join_code = serializer.save()
        return Response({
            "code": join_code.code,
            "expires_at": join_code.expires_at,
            "created_at": join_code.created_at
        }, status=status.HTTP_201_CREATED)


class ListOrganizationJoinCodesView(generics.ListAPIView):
    serializer_class = OrganizationJoinCodeListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        organization = user.organizations.first()
        return OrganizationJoinCode.objects.filter(organization=organization)

class UseJoinCodeView(generics.CreateAPIView):
    serializer_class = UseJoinCodeSerializer
    permission_classes = [permissions.IsAuthenticated]


class CheckActiveEmploymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        try:
            employment = Employment.objects.select_related('organization').get(user=user, end_date__isnull=True)
        except Employment.DoesNotExist:
            return Response({"detail": "Active employment not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrganizationSerializer(employment.organization)
        return Response(serializer.data)
