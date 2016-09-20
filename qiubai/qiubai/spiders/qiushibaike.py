# -*- coding: utf-8 -*-
import scrapy


class QiushibaikeSpider(scrapy.Spider):
    name = "qiushibaike"
    allowed_domains = ["qiushibaike.com"]
    start_urls = (
        'http://www.qiushibaike.com/',
    )

    def parse(self, response):
        print response.xpath('//div[@class = "content"]/span').extract()
        
