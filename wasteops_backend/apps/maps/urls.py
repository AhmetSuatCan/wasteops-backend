from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.maps.views import ContainerViewSet, RouteViewSet, RouteNodeBulkCreateAPIView

app_name = 'apps.maps'

router = DefaultRouter()
router.register(r'containers', ContainerViewSet, basename='container')
router.register(r'routes', RouteViewSet, basename='route')

urlpatterns = [
    path('', include(router.urls)),
    path('route-nodes/bulk/', RouteNodeBulkCreateAPIView.as_view(), name='route-node-bulk-create'),

]
