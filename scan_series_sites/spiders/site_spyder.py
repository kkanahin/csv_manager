from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scan_series_sites.items import ScanSeriesSitesItem
import re
class SeasonvarSpider(BaseSpider):
    name = "seasonvar"
    allowed_domains=["seasonvar.org"]
    start_urls = [
        "http://www.seasonvar.ru/"
    ]

    def parse(self,response):
        x= HtmlXPathSelector(response)
        items=[]
        day_news=x.select("//div[@class='film-list-block']")
        for each in day_news:
            item=ScanSeriesSitesItem()
            item['month']=each.select("div[@class='film-list-block-title']/div[@class='ff1']/text()").re("\d+\.(\d+.\d+)")
            item['day']=each.select("div[@class='film-list-block-title']/div[@class='ff1']/text()").re("(\d+)\.\d+.\d+")
            item['number_of_series']=len(each.select("div[@class='film-list-block-content']/div[@class='film-list-item']/text()"))
            items.append(item)
        return items
            