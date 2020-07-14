from django.db import models
from django.utils import timezone
# from datetime import date

# Create your models here.
''' This class contains a "service" that is nothing more \
     than a common electric meter.'''


class Meter(models.Model):
    name = models.CharField(max_length=50)
    ueb = models.ForeignKey('ueb', on_delete=models.CASCADE)
    month_plan = models.IntegerField()
    day_plan = models.IntegerField()
    higher_consumer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def totalConsumptionAtDay(self, day):
        amm = []
        for reading in Reading.objects.filter(date__day=day):
            amm.append(reading.consumption)
        return sum(amm)

    def consumptionPercentage(self, month):
        return (self.totalConsumptionAtMonth(month) * 100) / self.month_plan

    def totalConsumptionAtMonth(self, month):
        total = []
        for reading in Reading.objects.filter(date__month=month):
            total.append(reading.consumption)
        return sum(total)


class Reading(models.Model):
    date = models.DateTimeField(default=timezone.now)
    reading = models.PositiveIntegerField(default=0)
    consumption = models.IntegerField(default=0)
    for_meter = models.ForeignKey('Meter',
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  default=1)

    def __str__(self):
        return self.for_meter.name + str(self.date) + "  " + str(
            self.reading) + "  " + str(self.consumption)

    '''This function return the last reading in the database (query) , we\
         could have used the default model manager to access the record but we\
              want to keep things modular :P  '''

    def get_prev_reading(self):
        return Reading.objects.filter(
            for_meter=self.for_meter).last()

    def adjust_consumption(self, new_reading):
        pass

    '''Overriding save() method to calculate the real consumption '''

    def save(self, *args, **kwargs):
        last_record = self.get_prev_reading()
        # If there isn't previous record, then consumption goes to 0
        if last_record is None:
            self.consumption = 0
        else:
            # Some validation in the readings, by logic, there will be greater\
            #  than previous reading
            if self.reading > last_record.reading:
                self.consumption = self.reading - last_record.reading
            else:
                # If not, raise a ValueError (Validation Error ?) with\
                #  some message
                raise ValueError(
                    "La lectura que esta insertando debe ser mayor \
                         que la anterior, que es "
                    + str(last_record.reading))
        super().save(*args, **kwargs)


class Ueb(models.Model):
    name = models.CharField(max_length=50, default='UebSinNombre')

    def __str__(self):
        return self.name

    def totalConsumptionByUEB(self, for_ueb):
        total = []
        allbyueb = Reading.objects.filter(for_meter__ueb=for_ueb)

        for reading in allbyueb:
            total.append(reading.consumption)
        return sum(total)
