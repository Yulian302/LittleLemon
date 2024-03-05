import json

from django.test import TestCase
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuItemTest(TestCase):
    def test_create_item(self):
        item_name = "Mock item"
        price = 30
        item = Menu.objects.create(title=item_name, price=price, inventory=100)
        self.assertEqual(str(item), f"{item_name} : {price}")


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.menu_item = Menu.objects.create(title="Pizza", price=30, inventory=100)

    def mock_api(self):
        return {"id": 2, "title": "Pizza", "price": "30.00", "inventory": 100}

    def test_detail(self):
        serialized_data = MenuSerializer(self.menu_item).data
        response = self.mock_api()
        self.assertDictEqual(response, serialized_data)
