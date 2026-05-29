from django.test import TestCase
from django.urls import reverse, resolve

from users.views import (
    UserDetailView,
    UserRegisterView,
    UserActivateView,
    LogoutView
)


class UsersURLsTest(TestCase):
    def test_user_detail_url(self):
        self.assertEqual(
            resolve("/users/1/").func.view_class, UserDetailView
        )

    def test_register_url(self):

        self.assertEqual(
            resolve("/register/").func.view_class, UserRegisterView
        )

    def test_activate_url(self):
        self.assertEqual(
            resolve(
                "/activate/abc/token123/"
            ).func.view_class, UserActivateView
        )

    def test_logout_url(self):
        self.assertEqual(
            resolve("/logout/").func.view_class, LogoutView
        )

    def test_reverse_user_detail(self):
        self.assertEqual(
            reverse("users:user-detail", args=[1]), "/users/1/"
        )

    def test_reverse_register(self):
        self.assertEqual(
            reverse("users:register"), "/register/"
        )

    def test_reverse_logout(self):
        self.assertEqual(
            reverse("users:logout"), "/logout/"
        )
