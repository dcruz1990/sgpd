from os import name

from django.contrib.auth.models import User
from django.http import response
from django.http.request import bytes_to_text
from django.template import context
from django.test import client
from django.urls.base import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from energia.models import Meter, Reading, Ueb

import json


class MeterTests(APITestCase):

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
        data = {'name': 'TestMeter',
                'ueb': 1,
                'day_plan': 10,
                'month_plan': 300}
        url = "/api/meters/"
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_get_readings_by_month(self):
        """ Get all readings by given month """
        url = '/api/meters/1/readings_by_month/?month=10'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_uebs_endpoint_works(self):
        """ Get all uebs"""
        url = "/api/uebs/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_total_consumption_of_ueb_with_id_1(self): 
        """ Get total consumption of ueb with id 1"""
        url = "/api/uebs/1/totalconsumption/"
        response = self.client.get(url)
        self.assertEqual(response.data, { "name" : "TestUeb" , "consumption" : 0 })



