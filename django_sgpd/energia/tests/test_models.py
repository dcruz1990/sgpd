from datetime import date

from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from energia.models import Meter, Reading, Ueb


# Meter test case
class MeterTestCase(TestCase):
    def setUp(self):
        # Populating db whit some records
        Ueb.objects.create(name="CM")
        Ueb.objects.create(name="Manati")
        # TestMeter creation
        Meter.objects.create(name="TestMeter",
                             ueb=Ueb.objects.get(name="CM"),
                             month_plan=100,
                             day_plan=3)

        Meter.objects.create(name="MyMeter",
                             ueb=Ueb.objects.get(
                                 name="Manati"), month_plan=50, day_plan=10)

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

    def test_meter_return_total_month_consumption(self):
        """Meter can return their total consumption"""
        meter = Meter.objects.get(name="TestMeter")
        self.assertIs(meter.totalConsumptionAtMonth(10),
                      90)

    def test_meter_return_correct_percentage_of_consumption(self):
        """Return the percentage of consumption"""
        meter = Meter.objects.get(name="TestMeter")
        self.assertIsNot(meter.consumptionPercentage(
            date(2019, 10, 19).month), float(10))

    def test_if_the_current_reading_is_less_than_previous_raise_ValueError(self):
        Reading.objects.create(reading=50, date=date(
            year=2020, month=8, day=16), for_meter=Meter.objects.get(name="MyMeter"))

        with self.assertRaises(ValueError):
            Reading.objects.create(reading=15, date=date(
                year=2020, month=8, day=17), for_meter=Meter.objects.get(name="MyMeter"))


class ReadingTestCase(TestCase):
    def setUp(self):
        pass
