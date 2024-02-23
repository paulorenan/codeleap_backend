from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Career

class CareerTests(APITestCase):
    def setUp(self):
        self.career = Career.objects.create(username='testuser', title='Test Title', content='Test Content')

    def test_get_careers(self):
        url = reverse('career-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_career(self):
        url = reverse('career-list')
        data = {'username': 'newuser', 'title': 'New Title', 'content': 'New Content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Career.objects.count(), 2)

    def test_get_single_career(self):
        url = reverse('career-retrieve-update-destroy', kwargs={'pk': self.career.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Title')

    def test_update_career(self):
        url = reverse('career-retrieve-update-destroy', kwargs={'pk': self.career.pk})
        data = {'title': 'Updated Title', 'content': 'Updated Content'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.career.refresh_from_db()
        self.assertEqual(self.career.title, 'Updated Title')

    def test_delete_career(self):
        url = reverse('career-retrieve-update-destroy', kwargs={'pk': self.career.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Career.objects.count(), 0)

