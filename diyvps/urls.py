from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('homepage.urls')),
    path('machines/', include('booking.urls')),
    path('users/', include('users.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
