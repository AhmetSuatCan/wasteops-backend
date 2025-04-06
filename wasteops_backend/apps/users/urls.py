from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import UserRegistrationView, UserLoginView

app_name = 'apps.users'
urlpatterns = [
    # Version v1 API endpoints
    path('auth/', include([
        path('register/', UserRegistrationView.as_view(), name='register'),
        path('login/', UserLoginView.as_view(), name='login'),
    ])),

    path('token/', include([
        path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
        path('verify/', TokenVerifyView.as_view(), name='token-verify'),
    ])),
]
