from django import forms
from .models import Vendor

class newVendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ["Full_Name","Email_Address", "Phone", "Priority",]
        widgets = {
            "Full_Name" : forms.TextInput (attrs = {"class": "form-control"}),
            "Email_Address" : forms.EmailInput(attrs= {"class" : "form-control", "type" : "email"}),
            "Phone" : forms.NumberInput(attrs={"class": "form-control", "type" : "number"}),
            "Priority" : forms.Select(attrs={"class": "form-select form-control"})
        }
    
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        full_name = cleaned_data.get('Full_Name')
        email = cleaned_data ["Email_Address"]
        
        if full_name in [vendor.Full_Name for vendor in Vendor.objects.all()]:
            self.add_error('Full_Name', "Name already in use!!")
        if email in [vendor.Email_Address for vendor in Vendor.objects.all()]:
            self.add_error("Email_Address", "Email Already in use!")
    