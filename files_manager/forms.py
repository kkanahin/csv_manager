from django import forms
from files_manager.models import Category

class UploadFileForm(forms.Form):
    category=forms.ModelChoiceField(queryset=Category.objects.all(),initial="",\
        help_text="Select category")
    up_f=forms.FileField(label="Upload file")