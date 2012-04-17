from files_manager.models import CSVData
from files_manager.models import Category
from django.db import IntegrityError

def handle_uploaded_file(f,c):
    up_file_category=Category.objects.get(id=c)
    try:
        CSVData(name_file=f,category=up_file_category).save()
    except IntegrityError:
        return "file with that name already exists"
    return "upload success"
    