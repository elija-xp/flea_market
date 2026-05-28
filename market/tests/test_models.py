from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from market.models import Category, Deal, Item


User = get_user_model()


def create_user(username="testuser", password="testpass123"):
    return User.objects.create_user(username=username, password=password)


def create_category(name="Electronics"):
    return Category.objects.create(name=name)


def create_item(seller, category, title="Test Item", price="100.00"):
    return Item.objects.create(
        title=title,
        description="desc",
        price=Decimal(price),
        category=category,
        seller=seller,
    )


class CategoryModelTest(TestCase):
    def test_str(self):
        self.assertEqual(str(Category.objects.create(name="Books")), "Books")


class ItemModelTest(TestCase):
    def setUp(self):
        self.item = create_item(create_user(), create_category())

    def test_str(self):
        self.assertEqual(str(self.item), "Test Item")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.item.get_absolute_url(), f"/items/{self.item.pk}/"
        )


class DealModelTest(TestCase):
    def setUp(self):
        seller = create_user("seller")
        buyer = create_user("buyer")
        item = create_item(seller, create_category())
        self.deal = Deal.objects.create(item=item, buyer=buyer)

    def test_str(self):
        self.assertIn("-", str(self.deal))

    def test_deal_links_item_and_buyer(self):
        self.assertEqual(self.deal.item.title, "Test Item")
        self.assertEqual(self.deal.buyer.username, "buyer")
