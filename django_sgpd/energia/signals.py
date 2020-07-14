from django.db.models.signals import pre_save
from energia.models import Reading, Meter


def generate_consumption(sender, **kwargs):
    pass