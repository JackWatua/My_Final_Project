from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'inventory' : "Accurate , continous monitoring of your stock. Ensure that you have the right quantity and quality. Reduce Losses and Expenses. Automate Supply Chain Processes" ,
        'sales' : 'Manage leads, manage transactions, Evaluate sales',
        'purchases' : 'Manage purchases, Invoices, Orders, Analyze stock',
        'expenses' : 'Manage expenses, Track & minimize unnecessary expenses, Analyze expenses, identify bottlenecks',
        'vendors' : 'Manage Vendor relations, Analze vender transactions'
    }
    return render(request, 'landing.html', context)