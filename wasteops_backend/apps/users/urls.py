from django.urls import path
from .views import UserRegistrationView, UserLoginView

app_name = 'apps.users'
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]
