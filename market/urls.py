from django.urls import path

from market.views import (
    index,
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
    buy_item,
    toggle_wishlist,
    UserDetailView,
    logout_view,
    UserRegisterView,
    UserActivateView,
)

app_name = "market"

urlpatterns = [
    path(
        "",
        index,
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
        buy_item, name="buy-item"
    ),
    path(
        "items/<int:pk>/wishlist/",
        toggle_wishlist,
        name="toggle-wishlist"
    ),
    path(
        "users/<int:pk>/",
        UserDetailView.as_view(),
        name="user-detail"
    ),
    path(
        "logout/",
        logout_view,
        name="logout"
    ),
    path(
        "register/",
        UserRegisterView.as_view(),
        name="register"
    ),
    path(
        "activate/<str:uid>/<str:token>/",
        UserActivateView.as_view(),
        name="activate"
    ),
]
