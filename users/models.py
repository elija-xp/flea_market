from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=50, blank=True)

    def get_absolute_url(self):
        return reverse("users:user-detail", kwargs={"pk": self.pk})
