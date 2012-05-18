# Scrapy settings for scan_series_sites project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scan_series_sites'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['scan_series_sites.spiders']
NEWSPIDER_MODULE = 'scan_series_sites.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

