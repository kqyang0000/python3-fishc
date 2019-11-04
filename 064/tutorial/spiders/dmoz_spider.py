import scrapy
import os
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ['chinadmoz.org']
    start_urls = [
        'http://www.chinadmoz.org'
    ]

    def parse(self, response):
        path = '/Users/yangkaiqiang/Desktop/dmoz'
        # os.mkdir(path)
        # os.chdir(path)
        # filename = 'dmoz'
        # filename = response.url.split(".")[-2]
        # print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=" + filename)
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        items = []
        sel = scrapy.selector.Selector(response)
        sets = sel.xpath('//ul/li')
        for s in sets:
            item = DmozItem()
            item['title'] = s.xpath('a/text()').extract()
            item['link'] = s.xpath('a/@href').extract()
            item['desc'] = s.xpath('text()').extract()
            items.append(item)
        return items
