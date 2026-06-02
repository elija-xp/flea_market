from django.contrib.auth import get_user_model
from django.db import transaction

from users.services.email_service import UserEmailService
from users.services.errors import UserAlreadyExist

User = get_user_model()


class UserService:
    def __init__(self, email_service: UserEmailService | None = None):
        self._email_service = email_service or UserEmailService()

    def register_user(self, validated_data: dict, url: str) -> User:
        with transaction.atomic():
            if User.objects.filter(email=validated_data["email"]).exists():
                raise UserAlreadyExist(
                    f"User with email {validated_data['email']}"
                    f" already exists."
                )

            data = validated_data.copy()
            password = data.pop("password1")
            data.pop("password2")

            user = User.objects.create_user(
                **data, password=password, is_active=True
            )

        return user
