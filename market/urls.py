from django.urls import path

from market.views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
    ToggleWishlistView,
    BuyItemView, IndexView,
)

app_name = "market"

urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index"
    ),
    path(
        "items/",
        ItemListView.as_view(),
        name="item-list"
    ),
    path(
        "items/<int:pk>/",
        ItemDetailView.as_view(),
        name="item-detail"
    ),
    path(
        "items/create/",
        ItemCreateView.as_view(),
        name="item-create"
    ),
    path(
        "items/<int:pk>/update/",
        ItemUpdateView.as_view(),
        name="item-update"
    ),
    path(
        "items/<int:pk>/delete/",
        ItemDeleteView.as_view(),
        name="item-delete"
    ),
    path(
        "items/<int:pk>/buy/",
        BuyItemView.as_view(),
        name="buy-item"
    ),
    path(
        "items/<int:pk>/wishlist/",
        ToggleWishlistView.as_view(),
        name="toggle-wishlist"
    ),
]
