from files_manager.models import CSVData,Category,File_head
import re
from files_manager.tasks import upload_data
from django.conf import settings
import os

def handle_uploaded_file(csv_file,category):
    upload_category=Category.objects.get(id=category)
    upload_file=upload_category.csvdata_set.create(
                name_file=csv_file,
                upload_status='is_uploading'
                )
    file_ref=os.path.join(settings.MEDIA_ROOT,upload_file.name_file.url)
    upload_data.delay(upload_file,file_ref)
    return upload_file.id