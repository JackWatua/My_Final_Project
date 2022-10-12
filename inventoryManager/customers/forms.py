from django import forms
from .models import Customer


#All existing customers

Customers = Customer.objects.all()

class newCustomerForm(forms.Form):
    CUSTOMER_PRIORITY = (
        (1, 'High'),
        (2, 'Low'),
        (3, 'Moderate')
    )


    full_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control', 'type' : 'email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'number'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    priority = forms.ChoiceField(widget = forms.Select(attrs = {'class' : 'form-control form-select'}), choices=CUSTOMER_PRIORITY)



    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        full_name = cleaned_data.get('full_name')
        email = cleaned_data.get('email')
        
        if (full_name) in  [customer.Full_Name for customer in Customer.objects.all()]:
            self.add_error('full_name', '*Customer name already exists!')
        if email in [customer.Email_Address for customer in Customer.objects.all()]:
            self.add_error('email', '*Email already in use!')
        return cleaned_data


#Search form

class searchForm(forms.Form):
    search_item = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'search'}),label= '')



class filterForm(forms.Form):
    CHOICES = (
        ('1' , 'A-Z'),
        ('2', 'Priority')
    )

    filter_customers = forms.ChoiceField(widget = forms.Select(attrs={'class' : 'form-select form-control'}), choices=CHOICES)