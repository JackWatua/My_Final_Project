from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import newReportForm
from django.contrib import messages
from django.urls import reverse
import os
from django.conf import settings
from django.conf.urls.static import static
# Create your views here.


def reports(request):
    template = loader.get_template('reports.html')
    context = {}
    return HttpResponse(template.render(context, request))


def new_report(request):
    if request.method == 'POST':
        form = newReportForm(request.POST)
        if form.is_valid():
            #Upload report
            request.FILES["File"].name.split(".")[0] = request.POST.get("Report_title")
            save_path = os.path.join(settings.MEDIA_ROOT, "reports",request.FILES["File"].name)
            with open (save_path, "wb") as output :
                for chunk in request.FILES["File"].chunks():
                    output.write(chunk)
            form.save()
            messages.success(request, 'Report Added Successfully!')
            return HttpResponseRedirect(reverse('new_report'))

        else:
            pass
    else:
        form = newReportForm()
    context = {
        'form'  : form,
    }

    return render(request, 'new_report.html', context)


