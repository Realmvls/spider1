# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TencentPipeline(object):
    # def __init__ (self):
    #     self.f = open("tencent.json","w")
    #
    # def process_item(self, item, spider):
    #     try:
    #         content = json.dumps(dict(item),ensure_ascii = False) + ",\n"
    #         self.f.write(content)
    #         return item
    #     except Exception as e:
    #         print("文件写入出错",e)


    def close_spider(self,item,spider):
        return item
