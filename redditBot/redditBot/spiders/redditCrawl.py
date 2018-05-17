# -*- coding: utf-8 -*-
import scrapy

class RedditcrawlSpider(scrapy.Spider):
   	name = "redditCrawl"
   	start_urls = ['https://old.reddit.com/r/gameofthrones/']

   	def parse(self,response):
   		for row in response.css("div.thing"):
   			yield {
   				'title': row.css('a.title::text').extract_first(),
				'vote': row.css("div.unvoted::text").extract_first(),
				'created at': row.css('time::attr(title)').extract_first(),
				'comments': row.css('a.comments::text').extract_first(),
   			}
