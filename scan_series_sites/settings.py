# Scrapy settings for scan_series_sites project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import os

BOT_NAME = 'scan_series_sites'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['scan_series_sites.spiders']
NEWSPIDER_MODULE = 'scan_series_sites.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES=[
    'scan_series_sites.pipelines.ScanSeriesSitesPipeline',
     ]
     
def setup_django_env(path):
    import imp,os
    from django.core.management import setup_environ
    print path
    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)
    setup_environ(project)

scrapy_project_dir=os.path.realpath(os.path.dirname('__file__'))
print scrapy_project_dir
django_project_dir=os.path.join(scrapy_project_dir,'csv_manager')
setup_django_env(django_project_dir)