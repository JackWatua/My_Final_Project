from re import M
from django import forms
from .models import Report


class newReportForm (forms.ModelForm):
    class Meta:
        model = Report
        fields = ["Report_title" , "Report_Type", "File", "Date_Created",]
        widgets = {
            "Report_Type" : forms.Select(attrs= {"class" : "form-control form-select"}),
            "Report_title" : forms.TextInput(attrs = {"class" : "form-control", "type" : "text"}),
            "File" : forms.FileInput (attrs= {"class" : "file form-control", "type" : "file"}),
            "Date_Created" : forms.DateInput (attrs= {"class" : "form-control date", "type": "date"})
        }
    def clean (self, *args, **kwargs):
        cleaned_data = super().clean()
        title = cleaned_data.get("Report_title")
        if title in [report.Report_title for report in Report.objects.all()]:
            self.add_error("Report_title" , "Report_title already Exists!!")
        return cleaned_data
