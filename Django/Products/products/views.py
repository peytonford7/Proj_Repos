from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
from .models import Product

def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('products:product-list')
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, "products/product_create.html", context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }
    return render(request, "products/product_update.html", context)

def product_detail_view(request, id):
    print(f"Request for product ID: {id}")  # Debugging output
    obj = get_object_or_404(Product, id=id)
    print(f"Found product: {obj}")  # Debugging output
    context = {
        'object': obj,
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST request
    if request.method == "POST":
        # POST deleted 
        obj.delete()
        return redirect('products:product-list')
    context = {
        'object': obj,
    }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)