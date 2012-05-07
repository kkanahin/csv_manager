from django import forms
from files_manager.models import Category,CSVData
import re

#class UploadFileForm(forms.Form):
#    category=forms.ModelChoiceField(queryset=Category.objects.all(),initial="1",\
#        help_text="Select category")
#    upload_file=forms.FileField(label="Upload file",required=True)
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = CSVData
        fields = ('category','name_file')
    
    def clean_upload_file(self):
        data = self.cleaned_data['upload_file']
        check = re.compile('((\d+(\.)?(\d+)?)?(,|;))+\d+\.?(\d+)?(\n|\r\n)?')
        check_head=re.compile('([\w_-]+(,|;))+[\w_-]+(\n|\r\n)?')
        first_line_trig=0
        for line in data:
            if first_line_trig==0:
                if not check_head.match(line):
                    raise forms.ValidationError("The Head of this file is not right!")
                first_line_trig=1
            else:
                if not check.match(line):
                    raise forms.ValidationError("This file is not csv!")
        return data
