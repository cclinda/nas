# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    symbol=scrapy.Field()
    mkt = scrapy.Field()
    price = scrapy.Field()
    shares = scrapy.Field()
    offer = scrapy.Field()
    date = scrapy.Field()
    pass
