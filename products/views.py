from django.shortcuts import render

# Create your views here.
from .models import Product

def product_detail_view(request):
    obj= Product.objects.get(id=1)
    #content = {
    #   'title' : obj.title,
    #  'description': obj.description,
    #    'summary': obj.summary,
    #    'price': obj.price,

    #}
    content = {
        'object': obj
    }
    return render (request, "product/detail.html", content)
