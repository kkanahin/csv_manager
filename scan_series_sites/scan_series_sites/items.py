# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScanSeriesSitesItem(Item):
    # define the fields for your item here like:
    # name = Field()
    month=Field()
    day=Field()
    number_of_series=Field()
