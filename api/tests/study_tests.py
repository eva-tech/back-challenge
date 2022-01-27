from django.urls import reverse
from rest_framework import status
from django.test import TestCase

from api.models import Study


class StudyTestCase(TestCase):
    """
    Class to test Facility queries and mutations.
    """

    def test_create_study(self):
        url = reverse('studies')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Study.objects.count(), 1)
        self.assertEqual(Study.objects.get().name, 'DabApps')
