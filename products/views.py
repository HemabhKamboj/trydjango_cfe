from django.shortcuts import render

# Create your views here.
from .models import Product
from .forms import ProductForm, RawProductForm

def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
            
    context = {
        'form': my_form
    }
    return render (request, "product/product_create.html", context)

 
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
