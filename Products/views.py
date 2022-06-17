from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import os


def all_products(request):
    return render(request, "Products/all.html", {"products": Product.objects.all()})


def product_details(request, id):
    prod = get_object_or_404(Product, pk=id)
    return render(request, "Products/details.html", {"product": prod})


@login_required(login_url='login')
@staff_member_required(login_url='login')
def new(request):
    if request.method == "POST":
        formData = ProductForm(request.POST, request.FILES)
        if formData.is_valid():
            formData.save()
            return redirect("all_products")
    else:
        formData = ProductForm()
    return render(request, "Products/add.html", {"form": formData})


@login_required(login_url='login')
@staff_member_required(login_url='login')
def edit(request, id):
    prod = get_object_or_404(Product, pk=id)
    old_img = prod.image.path
    if request.method == "POST":
        formData = ProductForm(request.POST, request.FILES, instance=prod)
        if formData.is_valid():
            if 'image' in formData.changed_data and os.path.exists(old_img):
                os.remove(old_img)
            formData.save()
            return redirect("all_products")
    else:
        formData = ProductForm(instance=prod)
    return render(request, "Products/edit.html", {"form": formData, "product": prod})


@login_required(login_url='login')
@staff_member_required(login_url='login')
def delete(request, id):
    prod = Product.objects.get(pk=id)
    prod.image.delete()
    prod.delete()
    return HttpResponse("Success")
