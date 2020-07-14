from django.contrib import admin
from .models import Meter, Reading, Ueb

# Register your models here.
admin.site.register(Meter)
admin.site.register(Reading)
admin.site.register(Ueb)
