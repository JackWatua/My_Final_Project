from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import newExpenseForm
from .models import Expense

# Create your views here.


def expenses(request):
    template = loader.get_template('expenses.html')
    context = {
        'expenses' : Expense.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def new_expense(request):
    if request.method == 'POST':
        form = newExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense Added Successfully!')
            return HttpResponseRedirect(reverse('new_expense'))

        else:
            pass
    else:
        form = newExpenseForm()
    context = {
        'form'  : form,
    }

    return render(request, 'new_expense_form.html', context)