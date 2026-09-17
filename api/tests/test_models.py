from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Item

class ItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_create_item(self):
        item = Item.objects.create(title='Test Item', description='Test Description', owner=self.user)
        self.assertEqual(item.title, 'Test Item')
        self.assertFalse(item.completed)
        self.assertEqual(str(item), 'Test Item')