from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    UserCreateAPIView,
    UserDestroyAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
    PaymentsCreateAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path(
        "token/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="update_user"),
    path("delete/<int:pk>/", UserDestroyAPIView.as_view(), name="delete_user"),
    path("user/<int:pk>/", UserRetrieveAPIView.as_view(), name="user"),
    path("user_list/", UserListAPIView.as_view(), name="user_list"),
    path("payment_course/", PaymentsCreateAPIView.as_view(), name="payment_course"),
]
