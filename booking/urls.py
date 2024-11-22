from django.urls import path

import booking.views

urlpatterns = [
    path('', booking.views.listItems, name='listItems'),
]
