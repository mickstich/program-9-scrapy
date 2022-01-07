# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HolidaysItem(scrapy.Item):
    # define the fields for your item here like:
     Day = scrapy.Field()
     Date = scrapy.Field()
     Holiday_name = scrapy.Field()
     Type = scrapy.Field()
     comments = scrapy.Field()

