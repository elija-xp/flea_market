from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "phone", "city")
    fieldsets = UserAdmin.fieldsets + (
        ("Extra info", {"fields": ("phone", "city")}),
    )
