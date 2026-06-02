from django.urls import path

from users.views import (
    UserRegisterView,
    UserDetailView,
    LogoutView,
)

app_name = "users"

urlpatterns = [
    path(
        "users/<int:pk>/",
        UserDetailView.as_view(),
        name="user-detail"
    ),
    path(
        "register/",
        UserRegisterView.as_view(),
        name="register"
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout"
    ),
]
