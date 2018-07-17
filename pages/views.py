from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    print(request.user)
    return render (request, "home.html")


def contact_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "contact.html") 

def about_view(request, *args, **kwargs):
    print(request.user)
    my_context = {
        "title": "this is about us",
        "my_text": "this is about us",
        "my_number": 123,
        "my_list": [121, 123, 124],
        "my_html": "<h1>Hello World</h1>"
    }
    return render(request, "about.html", my_context)