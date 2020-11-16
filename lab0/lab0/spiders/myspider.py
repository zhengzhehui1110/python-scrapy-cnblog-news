# from tokenize import String

import scrapy
from scrapy import Selector

from lab0.items import ContentItem

from datetime import datetime
import time
import random
import re

import scrapy, json
from scrapy import Request

import urllib



class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['news.cnblogs.com']
    # start_urls = ['http://news.cnblogs.com/']
    start_urls = ['https://news.cnblogs.com/n/676871/']
    base_url = 'https://news.cnblogs.com/n/{}/'
    base_url_comment = 'https://news.cnblogs.com/news/comment?page={}'

    def start_requests(self):
        page_total = 200
        while (page_total != 0): # 爬取博客园最新评论页
            time.sleep(0.1)
            print(str(page_total))
            yield Request(self.base_url_comment.format(str(page_total)), callback=self.parse_comment)  # 填写url
            page_total = page_total - 1
        page_total = 7000
        lid = "67"
        while (page_total != 0):  # 爬取博客园新闻
            sublid = "{:0>4d}".format(page_total)
            time.sleep(0.1) # 每爬取一个页面的间隔时间
            print(sublid)
            page_total = page_total - 1
            yield Request(self.base_url.format(lid+sublid), callback=self.parse)  # 填写url







    def parse(self, response):
        # print(response.body)
        selector = Selector(response)
        # 在此，xpath会将所有class=topic的标签提取出来，当然这是个list
        # 这个list里的每一个元素都是我们要找的html标签
        content_list = selector.xpath("//*[@id='news_body']")
        # 遍历这个list，处理每一个标签
        for content in content_list:
            # 此处解析标签，提取出我们需要的帖子标题。
            topic = content.xpath('string(.)').extract_first()
            print (topic)
            item = ContentItem()
            item["content"] = topic
            item["author"] = ""  ## 略
            yield item

    def parse_comment(self, response):
        # print(response.body)
        selector = Selector(response)
        # 在此，xpath会将所有class=topic的标签提取出来，当然这是个list
        # 这个list里的每一个元素都是我们要找的html标签
        content_list = selector.xpath("//*[@class='comment_main']")
        # 遍历这个list，处理每一个标签
        for content in content_list:
            # 此处解析标签，提取出我们需要的帖子标题。
            topic = content.xpath('string(.)').extract_first()
            # print (topic)
            item = ContentItem()
            item["content"] = topic
            item["author"] = ""  ## 略
            yield item
