# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NyaaItem(scrapy.Item):
    # define the fields for your item here like:
    table = 'nyaa'
    name = scrapy.Field()
    magic = scrapy.Field()
    category = scrapy.Field()
    data = scrapy.Field()
    size = scrapy.Field()


