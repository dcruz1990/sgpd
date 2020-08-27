from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class MeterTests(APITestCase):
    
    def setUp(self):
        user = User.objects.create(username='dcruz')
        self.client.force_authenticate(user=user)
        
    
    def test_get_meter_list(self):
        """
        Ensure we can get meters 
        """
        url = "/api/meters/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_meter(self):
        """
        And we can create new meters 
        """
        data = {'name': 'DabApps'}
        url = "/api/meters/"
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
