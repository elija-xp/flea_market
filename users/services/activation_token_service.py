from django.contrib.auth.tokens import PasswordResetTokenGenerator


class ActivationTokenService(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (f"{user.pk}{user.password}{user.email}"
                f"{user.is_active}{timestamp}")


activation_token_service = ActivationTokenService()
