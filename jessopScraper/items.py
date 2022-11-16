# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JessopscraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    brand = scrapy.Field()
    link = scrapy.Field()
    image = scrapy.Field()
    price = scrapy.Field()
    about = scrapy.Field()
