
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.operations.views import (TeamViewSet,
                                   UserTeamViewSet,
                                   UnteamedEmployeesView,
                                   TeamMembersView,
                                   SoftRemoveUserTeamView,
                                   DisbandTeamView,
                                   ShiftViewSet,
                                   ShiftProgressViewSet,
                                   CreateShiftView,
                                   UpdateShiftEndTimeView)

app_name = 'apps.operations'

router = DefaultRouter()
router.register(r'team', TeamViewSet, basename='team')
router.register(r'teaming-employee', UserTeamViewSet, basename='user_team')
router.register(r'shift', ShiftViewSet, basename='shift')
router.register(r'shift-progress', ShiftProgressViewSet, basename='shift_progress')

urlpatterns = [
    path('', include(router.urls)),
    path('unteamed-employees/', UnteamedEmployeesView.as_view(), name='unteamed-employees'),
    path('team/<int:team_id>/members/', TeamMembersView.as_view(), name='team-members'),
    path('teaming-employee/<int:pk>/remove/', SoftRemoveUserTeamView.as_view(), name='userteam-soft-remove'),
    path('team/<int:pk>/disband/', DisbandTeamView.as_view(), name='team-disband'),
    path('create-shift/', CreateShiftView.as_view(), name='shift-create'),
    path('shift/<int:shift_id>/end/', UpdateShiftEndTimeView.as_view(), name='update-shift-end-time'),
]

