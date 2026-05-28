from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


def create_user(
        username="testuser",
        email="test@test.com",
        password="testpass123"
):
    return User.objects.create_user(
        username=username, email=email, password=password
    )


class UserModelTest(TestCase):
    def test_str(self):
        user = create_user()
        self.assertEqual(str(user), "testuser")

    def test_get_absolute_url(self):
        user = create_user()
        self.assertEqual(user.get_absolute_url(), f"/users/{user.pk}/")

    def test_phone_and_city_blank_by_default(self):
        user = create_user()
        self.assertEqual(user.phone, "")
        self.assertEqual(user.city, "")
