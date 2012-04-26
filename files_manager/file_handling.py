from files_manager.models import CSVData
from files_manager.models import Category
from django.db import IntegrityError
import re

def handle_uploaded_file(csv_file,category):
    upload_category=Category.objects.get(id=category)
    upload_file=upload_category.csvdata_set.create(
                name_file=csv_file,
                )
    for line in csv_file:
        value_splited=re.split(',|;',line.replace(',,',',0,'))
        func_variable_value=upload_file.func_var_set.create(
                            variable=value_splited[0],
                            )
        for variable_value in value_splited[1:]:
            func_variable_value.function_set.create(function=variable_value)
    return upload_file.id