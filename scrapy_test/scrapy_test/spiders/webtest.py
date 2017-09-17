# -*- coding: utf-8 -*-
#传智博客

import scrapy
from scrapy_test.items import webtestItem

class WebtestSpider(scrapy.Spider):
    name = "webtest"
    allowed_domains = ["www.itcast.cn"]
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#aandrold']

    def parse(self, response):
        data_list = response.xpath("//div[@class = 'li_txt']")
        items = []
        for data in data_list:
            item = webtestItem()
            name = data.xpath("./h3/text()").extract()
            title = data.xpath("./h4/text()").extract()
            info = data.xpath("./p/text()").extract()
            item['name']=name[0]
            item['title']=title[0]
            item['info']=info[0]
            items.append(item)
        return items
        # print(response.body)
        #pass
