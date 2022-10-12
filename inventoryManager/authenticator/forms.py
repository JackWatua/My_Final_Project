from dataclasses import fields
from django import forms

from authenticator.models import User


class logInForm(forms.Form):
    #Ask the user for their email address
    email_address = forms.EmailField(widget = forms.EmailInput(attrs = {
        'class' : 'form-control form-control-sm',
        'type': '<input type="submit" value="Sign Up" class="btn btn-danger btn-dark"><input type="submit" value="Sign Up" class="btn btn-danger btn-dark">',
        'placeholder' : 'sample@email.com'
    }))
    #Ask the user to enter their password to log in
    password = forms.CharField(widget= forms.PasswordInput(attrs = {
        'class' : 'form-control',
        'type' : 'password',
        'placeholder' : 'Password'
    }))



class signUpForm(forms.Form):
    #First name form input
    first_name = forms.CharField(widget= forms.PasswordInput(attrs = {
        'class' : 'form-control',
        'type' : 'text',
        'placeholder' : 'first name'
    }))
    #last name form input
    last_name = forms.CharField(widget= forms.TextInput(attrs = {
        'class' : 'form-control',
        'type' : 'text',
        'placeholder' : 'last name'
    }))

    #email address form input
    email_address = forms.EmailField(widget = forms.EmailInput(attrs = {
        'class' : 'form-control form-control-sm',
        'type': 'email',
        'placeholder' : 'sample@email.com'
    }))

    #password form input
    password = forms.CharField(widget= forms.PasswordInput(attrs = {
        'class' : 'form-control',
        'type' : 'password',
        'placeholder' : 'Password'
    }),min_length=8)
    #password confirmation form input
    confirm_password = forms.CharField(widget= forms.PasswordInput(attrs = {
        'class' : 'form-control',
        'type' : 'password',
        'placeholder' : 'confirm password'
    }))


    def clean(self, *args, **kwags):
        cleaned_data = super().clean()

        first_name = cleaned_data.get('first_name')
        last_name =  cleaned_data.get('last_name')
        email = cleaned_data.get('email_address')
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')

        #clean first name and last name 
        if not first_name.isalpha():
            self.add_error('first_name', 'First name must be alphabetical!')
        if not last_name.isalpha():
            self.add_error('last_name', 'Last name  must be alphabetical!')
        
        if password1 != password2 :
            self.add_error('confirm_password', 'Passwords do not match')
        
        if password1.isalpha():
            self.add_error('password', 'Password too weak!!')



