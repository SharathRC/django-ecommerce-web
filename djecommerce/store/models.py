from django.contrib.auth.models import User
from django.db import models
from django.core.files import File

from io import BytesIO
from PIL import Image
import numpy as np


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    DRAFT = "draft"
    WAITING_APPROVAL = "waiting_approval"
    ACTIVE = "active"
    DELETED = "deleted"

    STATUS_CHOICES = (
        (DRAFT, "Draft"),
        (WAITING_APPROVAL, "Waiting approval"),
        (ACTIVE, "Active"),
        (DELETED, "Deleted"),
    )

    user = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    description = models.TextField(blank=True)
    price = models.IntegerField()

    image = models.ImageField(
        upload_to="uploads/product_images/", blank=True, null=True
    )

    thumbnail = models.ImageField(
        upload_to="uploads/product_images/thumbnails/", blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title

    def get_display_price(self) -> float:
        return self.price / 100

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url

        if self.image:
            self.thumbnail = self.make_thumbnail(image=self.image)
            self.save()

            return self.thumbnail.url

        return "https://via.placehold.com/240x240x.jpg"

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size, Image.Resampling.NEAREST)

        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=80)

        name = image.name.replace("uploads/product_images/", "")
        thumbnail = File(thumb_io, name=name)

        return thumbnail

    def updated_thumbnail(self):
        self.thumbnail = self.make_thumbnail(image=self.image)
        self.save()


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    paid_amount = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    payment_intent = models.CharField(max_length=255)

    created_by = models.ForeignKey(
        User, related_name="orders", on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="items", on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_display_price(self) -> float:
        return self.price / 100
