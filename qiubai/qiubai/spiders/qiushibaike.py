# -*- coding: utf-8 -*-
import scrapy
from qiubai.items import  QiubaiItem

class QiushibaikeSpider(scrapy.Spider):
    name = "qiushibaike"
    allowed_domains = ["qiushibaike.com"]
    start_urls = (
        'http://www.qiushibaike.com/',
    )

    def parse(self, response):
        divs = '//div[@class = "article block untagged mb15"]'
        author_element = './div[@class = "author clearfix"]/a[2]/h2/text()'
        content_element = './a/div[@class = "content"]/span/text()'

        for ele in response.xpath(divs):
            items = QiubaiItem()
            items['author'] = ele.xpath(author_element).extract()
            items['content'] = ele.xpath(content_element).extract()
            print items['author'],items['content']
            yield items

            


