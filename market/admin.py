from django.contrib import admin

from market.models import Category, Item, Deal


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
