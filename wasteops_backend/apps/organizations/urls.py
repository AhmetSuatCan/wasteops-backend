from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrganizationViewSet,
    FacilityViewSet,
    CarViewSet,
    WasteContainerViewSet,
)

app_name = 'apps.organizations'

# Router setup
router = DefaultRouter()
router.register(r'core', OrganizationViewSet, basename='organization')
router.register(r'facilities', FacilityViewSet, basename='facility')
router.register(r'trucks', CarViewSet, basename='truck')
router.register(r'waste-containers', WasteContainerViewSet, basename='wastecontainer')

urlpatterns = [
    path('', include(router.urls)),
]
