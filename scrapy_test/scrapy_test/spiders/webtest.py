# -*- coding: utf-8 -*-
import scrapy


class WebtestSpider(scrapy.Spider):
    name = "webtest"
    allowed_domains = ["www.taobao.com"]
    start_urls = ['http://www.taobao.com/']

    def parse(self, response):
        print(response.body)
        #pass
