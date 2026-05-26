from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class UserEmailService:
    def send_activation_email(
        self,
        username: str,
        email: str,
        activation_link: str,
    ):
        html_content = render_to_string(
            "users/email/acc_active_email.html",
            context={
                "username": username,
                "activation_link": activation_link,
            }
        )
        message = EmailMessage(
            subject="Activate your account",
            body=html_content,
            to=[email],
        )
        message.content_subtype = "html"
        message.send()
