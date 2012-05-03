from files_manager.models import CSVData,Category,File_head
import re

def handle_uploaded_file(csv_file,category):
    upload_category=Category.objects.get(id=category)
    upload_file=upload_category.csvdata_set.create(
                name_file=csv_file,
                )
    first_line_trig=0
    for line in csv_file:
        if first_line_trig==0:
            head_splited=re.split(',|;',line.strip('\n\r'))
            for num_column,head in enumerate(head_splited):
                upload_file.file_head_set.create(column_number=num_column,\
                    column_head_str=head)
            first_line_trig=1
        else:
            value_splited=re.split(',|;',line.replace(',,',',0,'))
            func_variable_value=upload_file.func_var_set.create(
                                variable=value_splited[0],)
            for variable_value in value_splited[1:]:
                func_variable_value.function_set.create(function=variable_value)
    return upload_file.id