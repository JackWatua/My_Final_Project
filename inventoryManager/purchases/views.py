from .models import Purchase, purchaseTransaction
from .forms import newPurchaseForm
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from vendors.models import Vendor
# Create your views here.


def purchases(request):
    template = loader.get_template('purchases.html')
    context = {
        'items': purchaseTransaction.objects.all(),
        'vendors' : Vendor.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def create_transaction(cleaned_data):
    purchaseTransaction.objects.create(
        Item = cleaned_data['Item'],
        Quantity = cleaned_data['Quantity'],
        Price = cleaned_data['Price'],
        payment_method = cleaned_data['payment_method'],
    )

def new_purchase(request):
    if request.method == 'POST':
        form = newPurchaseForm(request.POST)
        if form.is_valid():
            #Get all cleaned data
            cleaned_data = form.cleaned_data
            #check if item already exists in purchased items
            if cleaned_data['Item'] in [p.Item for p in Purchase.objects.all()]:
                #Get the item
                item = Purchase.objects.get(Item = cleaned_data['Item'])
                #Check if price is equal to the existing item
                if cleaned_data['Price'] == item.Price:
                    #update item quantity
                    item.Quantity += cleaned_data['Quantity']
                    item.save()
                    #Create a new_purchase transaction record
                    create_transaction(cleaned_data)
                    messages.success(request, f"{cleaned_data['Item']} Price updated")
                    messages.success(request, f'{cleaned_data["Item"]}Purchase updated Successfully!')
                else:
                    item.Quantity += cleaned_data['Quantity']
                    item.save()
                    create_transaction(cleaned_data)
                    messages.success(request, f'Purchase updated Successfully!({cleaned_data["Item"]})')
                return HttpResponseRedirect(reverse('new_purchase'))
            else:
                form.save()
                create_transaction(cleaned_data)
                messages.success(request, 'New Purchase Added Successfully!')
                return HttpResponseRedirect(reverse('new_purchase'))
        else:
            pass
    else:
        form = newPurchaseForm()
    context = {
        'form'  : form,
    }

    return render(request, 'new_purchase_form.html', context)