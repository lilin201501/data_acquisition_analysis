# -*- coding: utf-8 -*-
import scrapy
from scrapytest01.items import Scrapytest01Item

class Test01Spider(scrapy.Spider):
    name = 'test01'
    allowed_domains = ['www.qidian.com']
    start_urls = ['http://www.qidian.com/rank/hotsales']

    def parse(self, response):

        # 存放书籍的集合
        book_items = []
        for each in response.xpath("//div[@class='book-mid-info']"):
            item = Scrapytest01Item()
            title = each.xpath("h4/a/text()").extract()[0]
            author = each.xpath("p/a[@class='name']/text()").extract()[0]
            abstract = each.xpath("p[@class='intro']/text()").extract()[0].strip()
            item['title'] = title
            item['author'] = author
            item['abstract'] = abstract

            book_items.append(item)

        return book_items
