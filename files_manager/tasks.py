from celery.decorators import task
import re

@task()
def upload_data(up_file_id, file_ref):
    csv_data=open(file_ref,'rb')
    first_line_trig=0
    for line in csv_data:
        if first_line_trig==0:
            head_splited=re.split(',|;',line.strip('\n\r'))
            for num_column,head in enumerate(head_splited):
                up_file_id.file_head_set.create(column_number=num_column,\
                    column_head_str=head)
            first_line_trig=1
        else:
            value_splited=re.split(',|;',line.replace(',,',',0,'))
            func_variable_value=up_file_id.func_var_set.create(
                                variable=value_splited[0],)
            for variable_value in value_splited[1:]:
                func_variable_value.function_set.create(function=variable_value)
    up_file_id.upload_status='uploaded'
    up_file_id.save()
    csv_data.close()