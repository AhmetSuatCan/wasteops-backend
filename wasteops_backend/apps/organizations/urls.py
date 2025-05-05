from django.urls import path, include
from .views import *

app_name = 'apps.organizations'

urlpatterns = [
    # Version v1 API endpoints
    path('core/', include([
        path('create/', OrganizationCreateAPIView.as_view(), name='create'),
        path('checkOrganization/', UserOrganizationRetrieveAPIView.as_view(), name='checkOrganization'),
    ])),
    path('facility/', include([
        path('create/', FacilityCreateAPIView.as_view(), name='create'),
        path('list/', FacilityListAPIView.as_view(), name='list'),
        path('<int:pk>/', FacilityRetrieveAPIView.as_view(), name='retrieve'),
        path('<int:pk>/delete/', FacilityDestroyAPIView.as_view(), name='destroy'),
    ])),
    path('car/', include([
        path('create/', CarCreateAPIView.as_view(), name='create'),
        path('list/', CarListAPIView.as_view(), name='list'),
        path('<int:pk>/', CarRetrieveAPIView.as_view(), name='retrieve'),
        path('<int:pk>/delete/', CarDestroyAPIView.as_view(), name='destroy'),
    ])),
    path('container/', include([
        path('create/', WasteContainerCreateAPIView.as_view(), name='create'),
        path('list/', WasteContainerListAPIView.as_view(), name='list'),
        path('<int:pk>/', WasteContainerRetrieveAPIView.as_view(), name='retrieve'),
        path('<int:pk>/delete/', WasteContainerDestroyAPIView.as_view(), name='destroy'),
    ])),
]
