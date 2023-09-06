from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify

from .models import UserProfile
from store.forms import ProductForm
from store.models import Product


def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    context = {"user": user}

    return render(request, "vendor_detail.html", context)


@login_required
def my_store(request):
    return render(request, "my_store.html")


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get("title")

            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            return redirect("my_store")
    else:
        form = ProductForm()

    context = {
        "title": "Add Product",
        "form": form,
    }

    return render(request, "add_product.html", context)


@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

        return redirect("my_store")
    else:
        form = ProductForm(instance=product)

    context = {
        "title": "Edit Product",
        "form": form,
    }
    return render(request, "add_product.html", context)


@login_required
def my_account(request):
    return render(request, "my_account.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            UserProfile.objects.create(user=user)

            return redirect("homepage")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})
