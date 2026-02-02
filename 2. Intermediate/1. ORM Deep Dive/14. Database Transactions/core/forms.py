from django import forms

from core.models import Rating, Restaurant, Order


class NumberOfItemsExceedsException(Exception):
    pass


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ("restaurant", "user", "rating")


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name", "restaurant_type")


class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


    def save(self, commit=True):
        number_of_items = self.cleaned_data['number_of_items']
        product = self.cleaned_data['product']

        if number_of_items > product.number_in_stock:
            raise NumberOfItemsExceedsException("Ordered number of items exceed the number in stock")
        
        return super().save(commit)
    
