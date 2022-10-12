from django import forms
from .models import Expense

class newExpenseForm (forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'Date' ,'Amount' ,'payment_method', 'expense_category']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'Date' : forms.DateInput(attrs={'class': 'form-control', 'type' : 'date', 'style' : 'width: fit-content'}),
            'Amount' : forms.NumberInput(attrs={'class' : 'form-control', 'type': 'number'}),
            'payment_method' : forms.Select(attrs={'class': 'form-control form-select'}),
            'expense_category' : forms.Select(attrs={'class' : 'form-select form-control'})
        }
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        amount  = cleaned_data.get('Amount')
        if amount  <= 0 :
            self.add_error('Amount', 'Amount cannot be less or equal to 0')
