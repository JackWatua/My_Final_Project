# Create your views here.
from re import template
from django.template import loader
from django.http import HttpResponse
from .forms import newSaleForm
# Create your views here.


def sales(request):
    template = loader.get_template('sales.html')
    context = {}
    return HttpResponse(template.render(context, request))





def new_sale(request):
    if request.method == "POST":
        form  = newSaleForm(request.POST)
    else:
        form = newSaleForm()

    context = {
        'form' : form,
    }

    template = loader.get_template('new_sale.html')
    return HttpResponse(template.render(context, request))