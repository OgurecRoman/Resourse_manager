from django.urls import path, include
from rest_framework import routers

from booking.views import (
    MachineViewSet,
    UserViewSet,
    GroupViewSet,
    BookingViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', GroupViewSet)
router.register(r'groups', UserViewSet)
router.register(r'machines', MachineViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
