import queue
from django import forms

from vendors.models import Vendor
from .models import Purchase

class newPurchaseForm(forms.ModelForm):
    class Meta :
        model = Purchase
        fields = ['Item', 'Quantity' , 'Price' , 'vendor' , 'payment_method']
        widgets = {
            'Item' : forms.TextInput(attrs={'class' : 'form-control', 'type' : 'text'}),
            'Quantity' : forms.NumberInput(attrs={'class': 'form-control', 'type' : 'number'}),
            'Price' : forms.NumberInput(attrs={'class': 'form-control', 'type' : 'number'}),
            'vendor' : forms.Select(attrs={'class': 'form-control form-select'}),
            'payment_method' : forms.Select(attrs={'class': 'form-control form-select'}),
        }
    
    
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('Quantity')
        price = cleaned_data.get('Price')

        #Check if quantity is less or equal to zero
        if quantity <= 0:
            self.add_error('Quantity', 'Quantity cannot be 0 or less')
        #Check if price is less or equal to zero
        if price <= 0: 
            self.add_error('Price', 'Price cannot be 0 or less')
        #CHECK IF ITEM EXISTS
        return cleaned_data