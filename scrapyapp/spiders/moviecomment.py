# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import MovieItem


class MoviecommentSpider(RedisCrawlSpider):
    name = 'moviecomment'
    allowed_domains = ['douban.com']
    # start_urls = ['http://douban.com/']  https://movie.douban.com/subject/26636712/comments?start=0&limit=20
    redis_key = 'moviecomment:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        comment = '//div[@class="comment-item"]//span[@class="short"]/text()'
        reviews = response.xpath(comment).extract()
        for review in reviews:
            item = MovieItem()
            item['comment'] = review.strip()
            yield item
