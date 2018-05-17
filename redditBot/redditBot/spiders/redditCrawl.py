# -*- coding: utf-8 -*-
import scrapy


class RedditcrawlSpider(scrapy.Spider):
    name = "redditCrawl"
    allowed_domains = ["www.reddit.com/r/gameofthrones/"]
    start_urls = (
        'http://www.www.reddit.com/r/gameofthrones//',
    )

    def parse(self, response):
        pass
