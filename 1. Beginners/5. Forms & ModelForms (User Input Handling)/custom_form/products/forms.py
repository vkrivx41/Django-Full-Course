from django import forms
from .models import Product, Seller


class SellerForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Enter the username."}),
        label="Username",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': "Enter the email."}),
        label="Email",
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Enter the phone number."}),
        label="Phone number",
    )
    categories = forms.MultipleChoiceField(
        choices=Seller.CATEGORY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Product Categories",
    )
    profit = forms.FloatField(
        widget=forms.NumberInput(attrs={'placeholder': "Enter the percentage profit."}),
        label="Profit",
    )
    contract = forms.ChoiceField(
        choices=Seller.CONTRACT_CHOICES,
        widget=forms.Select,
        label="Contract Type",
    )


    class Meta:
        model = Seller
        fields = ["username", "email", "phone_number", "categories", "profit", "contract"]

    def is_valid(self) -> bool:
        if super().is_valid():
            phone_number: str = self.cleaned_data.get("phone_number")
            profit: float = self.cleaned_data.get("profit")
            
            if not phone_number.isnumeric():
                self.add_error(field="phone_number", error=forms.ValidationError("Phone number must be only digits."))
                return False
            if len(phone_number) != 10:
                self.add_error(field="phone_number", error=forms.ValidationError("Phone number must be of 10 digits."))
                return False
            if profit < 0 or profit > 1:
                self.add_error(field="profit", error=forms.ValidationError("Profit must be a percentage between 0 and 1"))
                return False
        return True



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