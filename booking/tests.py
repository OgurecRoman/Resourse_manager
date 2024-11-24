from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class MachinesAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_machines_returns_200(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('machine-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_machines_unauthenticated(self):
        response = self.client.get(reverse('machine-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_machines_my_returns_200(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('machine-my'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_machines_available_returns_200(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('machine-available')
        url_with_query = f"{url}?start=2024-11-24-11:00&end=2024-11-24-12:00"
        response = self.client.get(url_with_query)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
