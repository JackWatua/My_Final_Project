# Create your views here.
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import newVendorForm
from .models import Vendor

from django.contrib import messages
# Create your views here.


def vendors(request):
    template = loader.get_template('vendors.html')
    vendors = Vendor.objects.all()
    context = {"vendors" : vendors }
    return HttpResponse(template.render(context, request))



def new_vendor(request):
    if request.method == "POST":
        form = newVendorForm (request.POST)
        if form.is_valid():
            messages.success(request, "Vendor added successfully!")
            form.save()
            return (HttpResponseRedirect(reverse("new_vendor")))
    else:
        form = newVendorForm()
    context = {
        "form" : form,
    }
    template = loader.get_template("new_vendor.html")

    return HttpResponse(template.render(context, request))