from django.urls import path, include
from rest_framework import routers

from homepage.views import HomepageViewSet

router = routers.DefaultRouter()
router.register(r'', HomepageViewSet, basename='homepage')

urlpatterns = [
    path('', include(router.urls)),
]
