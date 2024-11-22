from django.urls import path

import booking.views

urlpatterns = [
    path('book/<int:pk>/', booking.views.book, name='book'),
]
