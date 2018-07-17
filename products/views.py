from django.shortcuts import render

# Create your views here.
from .models import Product
from .forms import ProductForm

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    content = {
        'form': form
    }
    return render (request, "product/product_create.html", content)

 
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
