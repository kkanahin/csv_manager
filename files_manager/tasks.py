from celery.task import task,periodic_task
from celery.task.control import revoke
from celery.schedules import crontab
from files_manager.models import CSVData
import re

@task()
def upload_data(up_file_id):
    check = re.compile('((\d+(\.)?(\d+)?)?(,|;))+\d+\.?(\d+)?(\n|\r\n)?')
    check_head=re.compile('([\w_-]+(,|;))+[\w_-]+(\n|\r\n)?')
    parcing_file=CSVData.objects.get(id=up_file_id)
    print up_file_id
    print parcing_file.name_file.path
    csv_data=open(parcing_file.name_file.path,'rb')
    first_line_trig=0
    for line in csv_data:
        if first_line_trig==0:
            if not check_head.match(line):
                parcing_file.upload_status='header_fail'
                parcing_file.save()
                logger=upload_data.get_logger()
                logger.info("File has bad data header")
            else:
                head_splited=re.split(',|;',line.strip('\n\r'))
                for num_column,head in enumerate(head_splited):
                    parcing_file.file_head_set.create(column_number=num_column,\
                                                       column_head_str=head)
                first_line_trig=1
        else:
            if not check.match(line):
                parcing_file.upload_status='content_fail'
                parcing_file.save()
                logger=upload_data.get_logger()
                logger.info("File has bad content")
            else:
                value_splited=re.split(',|;',line.replace(',,',',0,'))
                func_variable_value=parcing_file.func_var_set.create(
                                                 variable=value_splited[0],)
                for variable_value in value_splited[1:]:
                    func_variable_value.function_set.\
                                            create(function=variable_value)
    parcing_file.upload_status='uploaded'
    parcing_file.save()
    csv_data.close()
    return 'file is uploaded successful'

@periodic_task(ignore_result=True, run_every=crontab(hour=1, minute=0))
def clean_fail_files():
    time_delta=datetime.datetime.now()-datetime.timedelta(days=1)
    CSVData.objects.filter(upload_date__lt=time_delta).\
        exclude(upload_status='uploaded').delete()
    return 'File remove succesful'