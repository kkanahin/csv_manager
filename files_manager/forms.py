from django import forms
from files_manager.models import CSVData

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = CSVData
        fields = ('category','name_file')
