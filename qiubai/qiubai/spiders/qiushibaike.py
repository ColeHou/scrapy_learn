# -*- coding: utf-8 -*-
import scrapy
from qiubai.items import  QiubaiItem
from scrapy.http import Request

class QiushibaikeSpider(scrapy.Spider):
    name = "qiushibaike"
    allowed_domains = ["qiushibaike.com"]
    start_urls = (
        'http://www.qiushibaike.com/',
    )

    def parse(self, response):
        divs = response.xpath('//div[@class = "article block untagged mb15"]')
        for div in divs:
            items = QiubaiItem()
            items['author'] = div.xpath('./div[@class = "author clearfix"]/a[2]/h2/text()').extract()[0]
            items['content'] = div.xpath('./a/div[@class = "content"]/text()').extract()[0]
            url = div.xpath('./a[@class= "contentHerf"]/@href').extract()[0]
            callbackUrl = response.urljoin(url)
            print callbackUrl, items['author'],items['content'] 
            yield Request(url = callbackUrl,callback = self.parse_comment, meta = {'item':items})

    def parse_comment(self,response):
        
        divs = response.xpath('//div[@class = "comments-table"]')
        for div in divs:
            items = response.meta['item']
            comment_author = div.xpath('./a/div/div[@class ="cmt-name"]/text()').extract()[0]
            comment_content = div.xpath('./a/div[@class = "main-text"]/text()').extract()[0]
            comment = {'comment_author':comment_author,'comment_content':comment_content}
            items['comment'] = comment
            print comment
            yield items
            
            


