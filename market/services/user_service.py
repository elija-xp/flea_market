from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from market.services.activation_token_service import activation_token_service
from market.services.email_service import UserEmailService
from market.services.errors import UserAlreadyExist

User = get_user_model()


class UserService:
    def __init__(self, email_service: UserEmailService | None = None):
        self._email_service = email_service or UserEmailService()

    @staticmethod
    def _encode_user_id(user_id: int) -> str:
        return urlsafe_base64_encode(str(user_id).encode())

    def register_user(self, validated_data: dict, url: str) -> User:
        with transaction.atomic():
            if User.objects.filter(email=validated_data["email"]).exists():
                raise UserAlreadyExist(
                    f"User with email {validated_data['email']} already exists."
                )

            data = validated_data.copy()
            password = data.pop("password1")
            data.pop("password2")

            user = User.objects.create_user(**data, password=password, is_active=False)
            token = activation_token_service.make_token(user)
            uid = self._encode_user_id(user.id)

            activation_link = f"{url}activate/{uid}/{token}/"
            self._email_service.send_activation_email(
                username=user.username,
                email=user.email,
                activation_link=activation_link,
            )

        return user

    def activate_user(self, uid: str, token: str) -> User:
        pk = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(pk=pk)

        if not activation_token_service.check_token(user, token):
            raise ValueError("Invalid or expired token")

        user.is_active = True
        user.save()
        return user
