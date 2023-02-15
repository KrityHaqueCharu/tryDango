from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product
from products.forms import ProductForm
# Create your views here.


def home_view(request):
    # print(request)
    # return HttpResponse("<h1>This is the home</h1>")
    context = {
        "text": "This is text",
        "my_number": 123,
        "my_list": [55, 44, 66, 77]
    }
    return render(request, "home.html", context)


def contact(*args, **kwargs):
    return HttpResponse("<h1>This is contact</h1>")


def about(request):
    return render(request, "contact.html", {})


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "products/product_details.html", context)
   
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_all(request):
    obj = Product.objects.all()
    context = {
        'object': obj
    }
    return render(request, "products/product_details_all.html", context)

def dynamic_lookup_view(request,my_id):
    obj=Product.objects.get(id=my_id)
    context ={
        "object":obj
    }
    return render(request, "products/product_details.html", context)
