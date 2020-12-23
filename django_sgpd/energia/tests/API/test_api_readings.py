
from django.contrib.auth.models import User
from django.http import response

from django.test import client
from django.urls.base import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from energia.models import Meter, Reading, Ueb


class ReadingTests(APITestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        self.client.force_authenticate(user=user)
        Ueb.objects.create(name="TestUeb")
        Meter.objects.create(name="FakeMeter",
                             ueb=Ueb.objects.get(name="TestUeb"),
                             month_plan=100,
                             day_plan=3)
        fakeMeter = Meter.objects.get(name="FakeMeter")
        Reading.objects.create(for_meter=fakeMeter, reading=1)
        Reading.objects.create(for_meter=fakeMeter, reading=10)
        Reading.objects.create(for_meter=fakeMeter, reading=20)

    def test_get_reading_list(self):
        """
        Ensure we can get Readings 
        """
        url = reverse('reading-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_reading(self):
        """
        And we can create new readings
        """
        data = {
            'for_meter': 1,
            'reading': 200
         }
        url = reverse('reading-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reading.objects.all().count(), 4)

        #If no meter exists?, going with an non existent meter id, get 400
        noMeterData = {
            'for_meter': 4,
            'reading': 200
        }
        response = self.client.post(url, noMeterData)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        

    def test_can_delete_a_reading(self):
        url = "http://localhost:8000/api/readings/1/" 
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_update_a_reading(self):
        data = { 'reading': 200  }
        url = "http://localhost:8000/api/readings/1/" 
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Reading.objects.get(pk=1).reading, 200)

    

        
   
    
    

    



