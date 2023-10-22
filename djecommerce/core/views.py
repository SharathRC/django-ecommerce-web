from django.shortcuts import render
from store.models import Product


def homepage(request):
    products = Product.objects.filter(status=Product.ACTIVE)
    context = {"products": products}

    return render(request, "homepage.html", context)


def about(request):
    return render(request, "about.html")
