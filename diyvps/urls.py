from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from tutorial.quickstart import views
from booking.views import MachineViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'machines', MachineViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    # path('', include("homepage.urls")),
    path('machines/', include("booking.urls")),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path(
        'api-auth/', include('rest_framework.urls', namespace='rest_framework')
    ),
]
