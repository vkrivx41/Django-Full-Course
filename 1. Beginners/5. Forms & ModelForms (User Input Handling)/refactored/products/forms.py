from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    available_colors = forms.MultipleChoiceField(
        choices=Product.COLOR_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Colors"
    )
    category = forms.ChoiceField(
        choices=Product.CATEGORY_CHOICES,
        widget=forms.Select(),
        required=False
    )


    class Meta:
        model = Product
        fields = ["product_name", "category", "available_colors", "price", "used", "promotion_date_ends"]

        widgets = {
            'available_colors': forms.CheckboxSelectMultiple,
            'promotion_date_ends': forms.DateInput(attrs={'type': "date"})
        }