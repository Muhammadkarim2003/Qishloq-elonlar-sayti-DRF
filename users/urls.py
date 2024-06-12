from .views import RegisterView, LoginAPIView, LogoutAPIView, UserListView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'api'

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/user-list/', UserListView.as_view()),
]