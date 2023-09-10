from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .cart import Cart
from .models import Product, Category


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect("cart_view")


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect("cart_view")


def cart_view(request):
    cart = Cart(request)

    context = {
        "cart": cart,
    }

    return render(request, "cart_view.html", context)


def search(request):
    query = request.GET.get("query", "")
    products = Product.objects.filter(status=Product.ACTIVE).filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )

    context = {
        "query": query,
        "products": products,
    }

    return render(request, "search.html", context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVE)
    context = {
        "category": category,
        "products": products,
    }

    return render(request, "category_detail.html", context)


def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)
    context = {"product": product}
    return render(request, "product_detail.html", context)
