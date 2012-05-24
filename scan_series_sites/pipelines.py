# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from files_manager.models import CSVData

class ScanSeriesSitesPipeline(object):
    def process_item(self, item, spider):
        print "#############################"
        print item
        return item
