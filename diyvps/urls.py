from django.urls import include, path
from django.contrib import admin

import booking.urls

urlpatterns = [
    path('', include(booking.urls.urlpatterns)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
