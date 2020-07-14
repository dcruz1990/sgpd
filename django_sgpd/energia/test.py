from django.test import TestCase
from django.utils import timezone
from datetime import date
# Create your tests here.
from .models import Meter, Ueb, Reading


# Meter test case
class MeterTestCase(TestCase):
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
        Reading.objects.create(date=date(2019, 8, 18),
                               reading=40,
                               for_meter=Meter.objects.get(name="TestMeter"))
        Reading.objects.create(date=date(2019, 10, 19),
                               reading=50,
                               for_meter=Meter.objects.get(name="TestMeter"))
        Reading.objects.create(date=timezone.now(),
                               reading=100,
                               for_meter=Meter.objects.get(name="TestMeter"))

    def test_meter_return_total_day_consumption_when_day_is_correct(self):
        """Meter can return their total consumption at some day when its correct"""
        meter = Meter.objects.get(name="TestMeter")
        self.assertIs(meter.totalConsumptionAtDay(date.today().day), 50)

    def test_meter_return_total_month_consumption(self):
        """Meter can return their total consumption"""
        meter = Meter.objects.get(name="TestMeter")
        self.assertIs(meter.totalConsumptionAtMonth(date(2019, 10, 19).month),
                      30)

    def test_meter_return_correct_percentage_of_consumption(self):
        """Return the percentage of consumption"""
        meter = Meter.objects.get(name="TestMeter")
        self.assertIs(meter.consumptionPercentage(
            date(2019, 10, 19).month), 10)


class ReadingTestCase(TestCase):
    def setUp(self):
        pass
