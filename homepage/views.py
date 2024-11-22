from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    template = "homepage/main.html"
    # return render(request, template)
    return HttpResponse("<h1>This is the home page</h1>")
