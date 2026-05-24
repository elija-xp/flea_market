from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=50, blank=True)

    def get_absolute_url(self):
        return reverse("market:user-detail", kwargs={"pk": self.pk})


class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="items"
    )
    wished_by = models.ManyToManyField(
        User, related_name="wishlist", blank=True
    )

    def get_absolute_url(self):
        return reverse("market:item-detail", kwargs={"pk": self.pk})


class Deal(models.Model):
    item = models.OneToOneField(
        Item, on_delete=models.CASCADE, related_name="deal"
    )
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="purchases"
    )
    created_at = models.DateTimeField(auto_now_add=True)
