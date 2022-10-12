from django import forms
from .models import Sale

class newSaleForm (forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['Item', 'Quantity', 'Price', 'payment_method', 'customer']
        widgets = {
            'Item' : forms.Select(attrs={'class': 'form-control form-select'}),
            'Quantity' : forms.NumberInput (attrs= {'class' : 'form-control', 'style' : 'width: fit-content'}),
            'Price' :  forms.NumberInput (attrs= {'class' : 'form-control', 'style' : 'width: fit-content', 'id' : 'Price'}),
            'payment_method' : forms.Select(attrs={'class': 'form-control form-select'}),
            'customer' : forms.Select(attrs={'class': 'form-control form-select', 'value' : '1'}),
        }