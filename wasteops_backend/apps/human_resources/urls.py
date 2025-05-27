from django.urls import path
from .views import (GenerateJoinCodeView,
                    UseJoinCodeView,
                    CheckActiveEmploymentView,
                    ListOrganizationJoinCodesView,
                    ListActiveOrganizationJoinCodesView,
                    ExpireJoinCodeView,
                    ListActiveEmployeesView,
                    EndEmploymentView)

app_name = 'apps.human_resources'
urlpatterns = [
    path('generate-code/', GenerateJoinCodeView.as_view(), name='generate_code'),
    path('expire-code/', ExpireJoinCodeView.as_view(), name='expire_code'),
    path('list-codes/', ListOrganizationJoinCodesView.as_view(), name='list_codes'),
    path('list-active-codes/', ListActiveOrganizationJoinCodesView.as_view(), name='list_active_codes'),
    path('use-code/', UseJoinCodeView.as_view(), name='use_code'),
    path('check-active-employment/', CheckActiveEmploymentView.as_view(), name='check_active_employment'),
    path('list-active-employees/', ListActiveEmployeesView.as_view(), name='check_active_employment'),
    path('end-employment/<uuid:user_id>/', EndEmploymentView.as_view(), name='end-employment'),
    # TODO:
     # path('create-team/', .as_view(), name='create-team'),
     # path('add-user-team/',.as_view(), name='add_user_team'),
     # path('delete-user-team/', .as_view(), name='delete_user_team'),
]
