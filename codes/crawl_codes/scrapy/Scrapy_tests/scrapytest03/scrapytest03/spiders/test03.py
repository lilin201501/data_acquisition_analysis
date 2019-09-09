# -*- coding: utf-8 -*-
import scrapy
import json
from scrapytest03.items import Scrapytest03Item

class Test03Spider(scrapy.Spider):
    name = 'test03'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/columns/zimei/articles?limit=20&offset=0']
    #print("dgdsg执行")
    def parse(self, response):
        print(response.body, "dsdgsdg中文")
        jsonBody = json.loads(response.body.decode('gbk').encode('utf-8'))
        articles = jsonBody['data']
        print(articles,"fdfsdfs")
        for art in articles:
            item = Scrapytest03Item()
            item['title'] = art['title']
            item['name'] = art['author']['name']
            item['headline'] = art['author']['headline']
            item['url'] = art['url']
            yield item

        if articles:
            yield scrapy.Request(jsonBody['paging']['next'], callback=self.parse)
        else:
            print("获取完毕！")
