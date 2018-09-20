# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedditbotItem(scrapy.Item):
    # define the fields for your item here like:
    tituloCampanha = scrapy.Field()
    arrecadado = scrapy.Field()
    objetivo = scrapy.Field()
    moeda = scrapy.Field()
    encerramento = scrapy.Field()
    contribuidores = scrapy.Field()
    historia = scrapy.Field()
    url = scrapy.Field()
