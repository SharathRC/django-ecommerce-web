import json
import stripe

from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse

from .cart import Cart
from .models import Product, Category, Order, OrderItem
from .forms import OrderForm


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect("cart_view")


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect("cart_view")


def change_quantity(request, product_id):
    cart = Cart(request)
    action = request.GET.get("action", "")
    if action:
        quantity = 1
        if action == "decrease":
            quantity = -1

        cart.add(product_id=product_id, quantity=quantity, update_quantity=True)

    return redirect("cart_view")


def cart_view(request):
    cart = Cart(request)

    context = {
        "cart": cart,
    }

    return render(request, "cart_view.html", context)


def invalid_checkout(request):
    return render(request, "invalid_checkout.html")


@login_required
def checkout(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            total_price = 0
            items = []

            for item in cart:
                product = item["product"]
                total_price += product.price * int(item["quantity"])

                items.append(
                    {
                        "price_data": {
                            "currency": "eur",
                            "product_data": {
                                "name": product.title,
                            },
                            "unit_amount": product.price,
                        },
                        "quantity": item["quantity"],
                    }
                )

            total_price_euro = total_price / 100
            if total_price_euro <= 0.5:
                return redirect("invalid_checkout")
            stripe.api_key = settings.STRIPE_SECRET_KEY
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=items,
                mode="payment",
                success_url="http://127.0.0.1:8002/cart/success/",
                cancel_url="http://127.0.0.1:8002/cart/",
            )
            payment_intent = session.payment_intent

            order = form.save(commit=False)
            order.created_by = request.user
            order.is_paid = True
            order.payment_intent = payment_intent
            order.paid_amount = total_price
            order.save()

            for item in cart:
                product = item["product"]
                price = product.price * int(item["quantity"])

                item = OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=price,
                    quantity=int(item["quantity"]),
                )

            cart.clear()

            # return redirect("homepage")
            return JsonResponse({"session": session, "order": payment_intent})
    else:
        form = OrderForm()

    context = {
        "cart": cart,
        "form": form,
        "pub_key": settings.STRIPE_PUB_KEY,
    }
    return render(request, "checkout.html", context)


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
