from django.urls import path, include
from .views import index

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('index/', index, name='index'),
]
