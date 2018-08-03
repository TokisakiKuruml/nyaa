# -*- coding: utf-8 -*-
import scrapy
from nyaa.items import NyaaItem
import time
class NySpider(scrapy.Spider):
    name = 'ny'
    allowed_domains = ['sukebei.nyaa.si']
    start_urls = ['https://sukebei.nyaa.si/']

    def parse(self, response):
        results = response.css('tbody tr')
        for result in results:
            item = NyaaItem()
            item['category'] = result.css('td a::attr(title)').extract_first()
            name = result.css('td[colspan="2"] a::text').extract_first()
            name = name.strip('\t\n\r')
            item['name'] = name
            magic = result.css('td[style="white-space: nowrap;"] a::attr(href)').extract()
            magic = magic[1].split('&')[0]
            item['magic'] = magic
            other = result.css('.text-center::text').extract()
            data = other[4]
            size = other[3]
            item['data'] = data
            item['size'] = size
            yield item
        next = response.css('.center li a[rel="next"]::attr(href)').extract_first()
        url2 = 'https://sukebei.nyaa.si'+next
        url3 = response.urljoin(url2)
        yield scrapy.Request(url=url3,callback=self.parse)




