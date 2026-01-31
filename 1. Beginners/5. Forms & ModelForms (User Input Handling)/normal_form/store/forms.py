from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .choices import ProductCategories


class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=200)
    product_category = forms.ChoiceField(choices=ProductCategories.choices)
    product_price = forms.IntegerField(min_value=0)
    warrant_months = forms.IntegerField(
        min_value=1, max_value=24,
        validators=[MinValueValidator(1), MaxValueValidator(24)]
    )
    is_used = forms.BooleanField(required=False)
    promotion_ends_date = forms.DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # modifying the input widgets and setting them to my desired one
        # a normal form doesn't have the Meta class
        # the choices must be repeated
        self.fields['product_name'].widget = forms.TextInput(attrs={'label': "Name"})
        self.fields['product_category'].widget = forms.Select(attrs={'label': "Category"}, choices=ProductCategories.choices)
        self.fields['product_price'].widget = forms.NumberInput(attrs={'label': "Price"})
        self.fields['warrant_months'].widget = forms.NumberInput(attrs={'label': "Warrant in Months"})
        self.fields['is_used'].widget = forms.CheckboxInput(attrs={'label': "Is Used"})
        self.fields['promotion_ends_date'].widget = forms.DateInput(attrs={'type': 'date'})