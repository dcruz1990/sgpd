from datetime import date

from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from energia.models import Meter, Reading, Ueb


# Meter test case
class ReadingTestCase(TestCase):
    def setUp(self):
        # Populating db whit some records
        Ueb.objects.create(name="CM")
        # TestMeter creation
        Meter.objects.create(name="TestMeter",
                             ueb=Ueb.objects.get(name="CM"),
                             month_plan=100,
                             day_plan=3)
        # Some readings, in different months and days
        Reading.objects.create(date=date(2019, 8, 17),
                               reading=10,
                               for_meter=Meter.objects.get(name="TestMeter"))
        Reading.objects.create(date=date(2019, 10, 19),
                               reading=50,
                               for_meter=Meter.objects.get(name="TestMeter"))
        Reading.objects.create(date=timezone.now(),
                               reading=100,
                               for_meter=Meter.objects.get(name="TestMeter"))

    def test_if_we_can_get_previous_reading(self):
        prev = Reading.objects.get(pk=1)
        self.assertEqual(100, prev.get_prev_reading().reading)

    

