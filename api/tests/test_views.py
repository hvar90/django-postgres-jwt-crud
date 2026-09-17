from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Item


class ItemAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password123')
        self.item = Item.objects.create(title='Initial Item', owner=self.user)
        self.list_url = reverse('item-list')

        # Obtener Token JWT usando la ruta directa o reverse
        res = self.client.post(reverse('token_obtain_pair'), {
                               'username': 'testuser', 'password': 'password123'})
        self.token = res.data['access']

    def test_get_items_unauthorized(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_items_authorized(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_item(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        data = {'title': 'New API Item', 'description': 'Created via test'}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)


""" 
        def perform_create(self, serializer):
            # Asigna automáticamente al usuario dueño basándose en el token JWT de la petición
             serializer.save(owner=self.request.user)
 """
