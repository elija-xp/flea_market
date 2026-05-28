from django.test import TestCase
from django.urls import reverse, resolve

from market.views import (
    IndexView,
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
    BuyItemView,
    ToggleWishlistView,
)


class MarketURLsTest(TestCase):
    def test_index_url(self):
        self.assertEqual(
            resolve("/").func.view_class, IndexView
        )

    def test_item_list_url(self):
        self.assertEqual(
            resolve("/items/").func.view_class, ItemListView
        )

    def test_item_detail_url(self):
        self.assertEqual(
            resolve("/items/1/").func.view_class, ItemDetailView
        )

    def test_item_create_url(self):
        self.assertEqual(
            resolve("/items/create/").func.view_class, ItemCreateView
        )

    def test_item_update_url(self):
        self.assertEqual(
            resolve("/items/1/update/").func.view_class, ItemUpdateView
        )

    def test_item_delete_url(self):
        self.assertEqual(
            resolve("/items/1/delete/").func.view_class, ItemDeleteView
        )

    def test_buy_item_url(self):
        self.assertEqual(
            resolve("/items/1/buy/").func.view_class, BuyItemView
        )

    def test_toggle_wishlist_url(self):
        self.assertEqual(
            resolve("/items/1/wishlist/").func.view_class, ToggleWishlistView
        )

    def test_reverse_index(self):
        self.assertEqual(
            reverse("market:index"), "/"
        )

    def test_reverse_item_list(self):
        self.assertEqual(
            reverse("market:item-list"), "/items/"
        )
