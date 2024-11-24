from django.shortcuts import render
from rest_framework import viewsets


class HomepageViewSet(viewsets.ViewSet):
    def list(self, request):
        context = {
            'title': 'Главная страница',
        }
        return render(request, 'homepage.html', context)
