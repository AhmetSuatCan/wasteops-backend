from django.urls import path
from .views import GenerateJoinCodeView, UseJoinCodeView, CheckActiveEmploymentView, ListOrganizationJoinCodesView 

app_name = 'apps.human_resources'
urlpatterns = [
    path('generate-code/', GenerateJoinCodeView.as_view(), name='generate_code'),
    path('list-codes/', ListOrganizationJoinCodesView.as_view(), name='list_codes'),
    path('use-code/', UseJoinCodeView.as_view(), name='use_code'),
    path('check-active-employment/', CheckActiveEmploymentView.as_view(), name='check_active_employment'),
    # TODO:
     # path('end-employment/', .as_view(), name='end_employment'),
     # path('create-team/', .as_view(), name='create-team'),
     # path('add-user-team/',.as_view(), name='add_user_team'),
     # path('delete-user-team/', .as_view(), name='delete_user_team'),
]
