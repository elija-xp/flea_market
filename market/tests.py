from decimal import Decimal
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from market.models import Category, Item, Deal

User = get_user_model()


def create_user(username="testuser", password="testpass123"):
    return User.objects.create_user(username=username, password=password)

def create_category(name="Electronics"):
    return Category.objects.create(name=name)

def create_item(seller, category, title="Test Item", price="100.00"):
    return Item.objects.create(
        title=title, description="desc",
        price=Decimal(price), category=category, seller=seller,
    )


class CategoryModelTest(TestCase):
    def test_str(self):
        self.assertEqual(str(create_category("Books")), "Books")


class IndexViewTest(TestCase):
    def test_index(self):
        response = self.client.get(reverse("market:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("num_items", response.context)


class ItemListViewTest(TestCase):
    def setUp(self):
        user, cat = create_user(), create_category()
        create_item(user, cat, title="Laptop")
        create_item(user, cat, title="Phone")
        self.cat = cat

    def test_search(self):
        r = self.client.get(reverse("market:item-list"), {"title": "Laptop"})
        self.assertContains(r, "Laptop")
        self.assertNotContains(r, "Phone")

    def test_filter_by_category(self):
        other = create_category("Furniture")
        create_item(create_user("u2"), other, title="Chair")
        r = self.client.get(reverse("market:item-list"), {"category": self.cat.pk})
        self.assertContains(r, "Laptop")
        self.assertNotContains(r, "Chair")


class ItemCreateViewTest(TestCase):
    def setUp(self):
        self.user = create_user()
        self.category = create_category()
        self.client.login(username="testuser", password="testpass123")

    def test_create_item(self):
        self.client.post(reverse("market:item-create"), {
            "title": "New Item", "description": "desc",
            "price": "50.00", "category": self.category.pk,
        })
        item = Item.objects.get(title="New Item")
        self.assertEqual(item.seller, self.user)


class BuyItemViewTest(TestCase):
    def setUp(self):
        self.seller = create_user("seller")
        self.buyer = create_user("buyer")
        self.item = create_item(self.seller, create_category())

    def test_buy_creates_deal(self):
        self.client.login(username="buyer", password="testpass123")
        self.client.get(reverse("market:buy-item", args=[self.item.pk]))
        self.assertTrue(Deal.objects.filter(item=self.item, buyer=self.buyer).exists())


class WishlistViewTest(TestCase):
    def setUp(self):
        self.user = create_user()
        self.item = create_item(create_user("seller"), create_category())
        self.client.login(username="testuser", password="testpass123")

    def test_toggle_wishlist(self):
        self.client.get(reverse("market:toggle-wishlist", args=[self.item.pk]))
        self.assertIn(self.item, self.user.wishlist.all())

        self.client.get(reverse("market:toggle-wishlist", args=[self.item.pk]))
        self.assertNotIn(self.item, self.user.wishlist.all())
