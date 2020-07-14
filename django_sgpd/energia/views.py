from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Meter, Ueb, Reading

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html', {'services': Meter.objects.all().count(),
                                          'readings': Reading.objects.all().count(),
                                          'ueb': Ueb.objects.all().count()
                                          })
