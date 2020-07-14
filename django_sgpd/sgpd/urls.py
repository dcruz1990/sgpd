from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from energia.api import MeterViewSet, UebViewSet, ReadingViewSet
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'meters', MeterViewSet)
router.register(r'uebs', UebViewSet)
router.register(r'readings', ReadingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('energia/', include('energia.urls')),
    path('api/', include(router.urls), name="Energia API"),
    # path('api/auth/', include('rest_framework.urls',
    #  namespace='rest_framework'))
    path('api/auth/login/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/auth/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
