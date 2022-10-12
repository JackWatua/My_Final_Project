from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import newCustomerForm, searchForm , filterForm
from django.urls import reverse
from django.contrib import messages
from .models import Customer
# Create your views here.










def customers(request):
    search_form = searchForm()
    filter_form = filterForm()
    form = newCustomerForm()
    all_customers = Customer.objects.all()
    context = {
        'form' : form,
        'search_form': search_form,
        'filter_form' : filter_form,
        'Customers' : all_customers,
    }
    return render(request, 'index.html', context)



def test(request):
    if request.method == 'POST':
        form = newCustomerForm(request.POST)
        if form.is_valid():
            all_data = form.cleaned_data
            Customer.objects.create(
                Full_Name = all_data['full_name'],
                Email_Address = all_data['email'],
                Phone = all_data['phone'],
                customer_priority = all_data['priority']
            )
            messages.success(request, 'Contact Created Successfully!')
            return HttpResponseRedirect(reverse('test'))

        else:
            pass
    else:
        form = newCustomerForm()
    context = {
        'demo' : 'demo()',
        'form'  : form,
    }

    return render(request, 'test.html', context)