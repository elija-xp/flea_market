from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from market.models import User, Category, Item, Deal


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "phone", "city")
    fieldsets = UserAdmin.fieldsets + (
        ("Extra info", {"fields": ("phone", "city")}),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "category", "seller", "created_at")
    list_filter = ("category",)
    search_fields = ("title",)


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ("id", "item", "buyer", "created_at")
