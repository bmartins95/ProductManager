from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def product_create_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../../")

    context = {
        "form": form
    }
    return render(request, "product_create.html", context)

def product_delete_view(request, id=1):
    pdt = get_object_or_404(Product, id=id)
    if request.method == "POST":
        pdt.delete()
        return redirect("../../")

    context = {
        "product": pdt
    }
    return render(request, "product_delete.html", context)

def product_list_view(request, *args, **kwargs):
    pdt = Product.objects.all()

    context = {
        "products": pdt
    }
    return render(request, "product_list.html", context)

def product_detail_view(request, id):
    pdt = get_object_or_404(Product, id=id)

    context = {
        "product": pdt
    }
    return render(request, "product_detail.html", context)
