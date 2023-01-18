from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Food


class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_food = Food.objects.create(type="Olives", purchaser=testuser1, description="Kalamata pitted")
        test_food.save()

    def test_food_model(self):
        food = Food.objects.get(id=1)
        actual_owner = str(food.purchaser)
        actual_name = str(food.type)
        actual_description = str(food.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Olives")
        self.assertEqual(actual_description, "Kalamata pitted")
