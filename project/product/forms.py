from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Product


class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'category',
            'price',
            'quantity',
        ]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return name


class ProductCrForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name','description','category','price','quantity',
