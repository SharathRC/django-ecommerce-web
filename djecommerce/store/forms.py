from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "category",
            "title",
            "description",
            "price",
            "image",
        )
        widgets = {
            "category": forms.Select(
                attrs={
                    "class": "w-full px-3 py-2 my-2 border border-gray-200",
                }
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 my-2 border border-gray-200",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 my-2 border border-gray-200",
                    "rows": 3,
                }
            ),
            "price": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 my-2 border border-gray-200",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "w-full px-3 py-2 my-2 border border-gray-200",
                }
            ),
        }
