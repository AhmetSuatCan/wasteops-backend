# apps.human_resources.views.py
from drf_yasg.utils import swagger_auto_schema
from django.utils import timezone
from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from apps.human_resources.models import OrganizationJoinCode
from rest_framework.response import Response
from apps.human_resources.models import Employment
from rest_framework.permissions import IsAuthenticated
from apps.users.permissions import IsAdmin
from apps.organizations.serializers import OrganizationSerializer
from apps.human_resources.serializers import (GenerateJoinCodeSerializer,
                                              UseJoinCodeSerializer,
                                              OrganizationJoinCodeListSerializer,
                                              ExpireJoinCodeSerializer,
                                              ActiveEmploymentSerializer,
                                              EndEmploymentSerializer)

'''
These two views is for generating a joining code to create an Employment.

An employment is basically a connection between a User and Organization.
'''


class GenerateJoinCodeView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

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
    permission_classes = [IsAuthenticated, IsAdmin]

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


class ListActiveOrganizationJoinCodesView(generics.ListAPIView):
    serializer_class = OrganizationJoinCodeListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        organization = user.organizations.first()
        now = timezone.now()
        return OrganizationJoinCode.objects.filter(
            organization=organization,
            is_revoked=False
        ).filter(
            Q(expires_at__isnull=True) | Q(expires_at__gt=now))


class ExpireJoinCodeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ExpireJoinCodeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        join_code = serializer.save()
        return Response({
            "detail": f"Join code '{join_code.code}' has been expired.",
            "expires_at": join_code.expires_at
        }, status=status.HTTP_200_OK)


class ListActiveEmployeesView(generics.ListAPIView):
    serializer_class = ActiveEmploymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        organization = user.organizations.first()

        if not organization:
            return Employment.objects.none()

        return Employment.objects.filter(
            organization=organization,
            end_date__isnull=True
        ).select_related('user')


class EndEmploymentView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    @swagger_auto_schema(request_body=EndEmploymentSerializer)
    def post(self, request, user_id):
        serializer = EndEmploymentSerializer(data={'user_id': user_id}, context={'request': request})
        if serializer.is_valid():
            employment = serializer.save()
            return Response(
                {"message": f"Employment for user {employment.user.email} ended."},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
