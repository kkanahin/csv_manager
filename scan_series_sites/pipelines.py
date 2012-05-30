# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from files_manager.models import CSVData,Category,Func_var,Function

class ScanSeriesSitesPipeline(object):
    def process_item(self, item, spider):
        try:
            query_category=Category.objects.get(name_category='seasonvar.ru')
        except Category.DoesNotExist:
            query_category=Category(name_category='seasonvar.ru')
            query_category.save()
        try:
            month=CSVData.objects.get(name_file=item['month'][0])
        except CSVData.DoesNotExist:
           month=query_category.csvdata_set.create(name_file=item['month'][0],\
               upload_status='uploaded',owner_id=1)
           month.file_head_set.create(column_number=0,column_head_str='day')
           month.file_head_set.create(column_number=1,column_head_str='num. of series')
        try:
            day=month.func_var_set.get(variable=item['day'][0])
        except Func_var.DoesNotExist:
            day=month.func_var_set.create(variable=item['day'][0])
            day.function_set.create(function=item['number_of_series'])
        return item
