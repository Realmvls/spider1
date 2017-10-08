# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    start_urls = ['http://tencent.com/']
    baseURL = "http://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [baseURL+str(offset)]
    def parse(self, response):
        node_list = response.xpath("//tr[@class='even']|//tr[@class='odd']")

        for node in node_list:
            item = TencentItem()                      #.extract()作用:内容转换为字符串
            if len(node.xpath("./td[1]/a/text()")):
                item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0].encode("utf-8")
            else:
                item['positionName'] = ""
            if len(node.xpath("./td[1]/a/@href")):
                item['positionLink']= node.xpath("./td[1]/a/@href").extract()[0].encode("utf-8")
            else:
                item['positionLink'] = ""
            if len(node.xpath("./td[2]/text()")):
                item['positionType'] = node.xpath("./td[2]/text()").extract()[0].encode("utf-8")
            else:
                item['positionType'] = ""
            item['positionNumber'] = node.xpath("./td[3]/text()").extract()[0].encode("utf-8")
            item['workLocation'] = node.xpath("./td[4]/text()").extract()[0].encode("utf-8")
            item['publishTime'] = node.xpath("./td[5]/text()").extract()[0].encode("utf-8")

            yield item
        if self.offset < 2190:
            self.offset += 10
            url = self.baseURL + str(self.offset)
            yield scrapy.Request(url,callback = self.parse)