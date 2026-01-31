from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Product
from .choices import ProductCategories


class ProductForm(forms.ModelForm):
    product_category = forms.ChoiceField(choices=ProductCategories.choices)

    class Meta:
        model = Product
        fields = ["product_name", "product_category", "product_price", "warrant_months", "is_used", "promotion_ends_date"]

        widgets = {
            'product_name': forms.TextInput(attrs={'label': "Name"}),
            'product_category': forms.Select(attrs={'label': "Category"}),
            'product_price': forms.NumberInput(attrs={'label': "Price"}),
            'warrant_months': forms.NumberInput(attrs={'label': "Warrant in Months"}),
            'is_used': forms.CheckboxInput(attrs={'label': "Is Used"}),
            'promotion_ends_date': forms.DateInput(attrs={'type': 'date'}),
        }