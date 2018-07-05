from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h1> Hello World </h1>")


def contact_view(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h1> Contact Page </h1>")