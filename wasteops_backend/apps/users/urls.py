from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import UserRegistrationView, UserLoginView, LogoutView, UserProfileView, WebLoginView, ValidateCookieTokenView

app_name = 'apps.users'
urlpatterns = [
    # Version v1 API endpoints
    path('me/', UserProfileView.as_view(), name='online_user_info'),
    path('auth/', include([
        path('register/', UserRegistrationView.as_view(), name='register'),
        path('login/', UserLoginView.as_view(), name='login'),
        path('web-login/', WebLoginView.as_view(), name='web-login'),
        path('check-token/', ValidateCookieTokenView.as_view(), name='check-token'),
        path('logout/', LogoutView.as_view(), name='logout'),
    ])),

    path('token/', include([
        path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
        path('verify/', TokenVerifyView.as_view(), name='token-verify'),
    ])),
]
