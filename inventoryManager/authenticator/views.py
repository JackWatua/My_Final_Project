from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import signUpForm, logInForm
from .models import User


# Create your views here.
def login(request):
    if request.method == 'GET':
        form = logInForm(request.GET)
        if form.is_valid():
            user_email = form.cleaned_data['email_address']
            password = form.cleaned_data['password']
            return HttpResponse(auth_user(user_email, password))
    else:
        form = logInForm()
    context = {'form' : form}
    template = loader.get_template('login.html')
    return HttpResponse(template.render(context, request))



def signup(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
            email = form.cleaned_data['email_address']
            phone = 712345678
            password = form.cleaned_data ['password']
            new_user = User.objects.create(name = name, email =email, phone =  phone, password = password)
            new_user.save()
    else:
        form = signUpForm()
    context = {'form' : form}
    template = loader.get_template('signup.html')
    return HttpResponse(template.render(context, request))





def auth_user(user_email, password):
    user_emails = [user.email for user in User.objects.all()]
    if user_email not in user_emails:
        return 'user not available'
    else:
        user = User.objects.get(email = user_email)
        if password != user.password :
            return 'Invalid Password!!'
        else:
            return 'Log in Successful!!'