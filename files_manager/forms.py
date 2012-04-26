from django import forms
from files_manager.models import Category
import re

class UploadFileForm(forms.Form):
    category=forms.ModelChoiceField(queryset=Category.objects.all(),initial="1",\
        help_text="Select category")
    upload_file=forms.FileField(label="Upload file",required=True)
    
    def clean_upload_file(self):
        data=self.cleaned_data['upload_file']
        check=re.compile('((\d+(\.|\;)?(\d+)?)?(,|;))+\d+\.?(\d+)?(\n|\r\n)?')
        for line in data:
            if not check.match(line):
                raise forms.ValidationError("This file is not csv!")
        return data
