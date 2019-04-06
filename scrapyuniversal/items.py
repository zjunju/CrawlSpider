# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


class ScrapyuniversalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewsItem(scrapy.Item):
    title = scrapy.Field()      # 文章标题
    url = scrapy.Field()        # 文章链接
    datetime = scrapy.Field()   # 文章发布时间
    source = scrapy.Field()     # 文章来源（在文章的发布时间旁）
    website = scrapy.Field()    # 站点名称，记录文章的站点
    content =scrapy.Field()     # 文章内容


class DefaultLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChinaLoader(DefaultLoader):
    content_out = Compose(Join(), lambda s:s.strip())
    source_out = Compose(Join(), lambda s: s.strip())


class QsbkItem(scrapy.Item):
    title = scrapy.Field()
    funny = scrapy.Field()
    datetime = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    auth = scrapy.Field()
    website = scrapy.Field()

class QsbkLoader(ItemLoader):
    default_output_processor = Compose(TakeFirst(),lambda s: s.strip())
    content_out = Compose(Join(), lambda s: s.strip())

# auth = response.xpath("//div[@class='side-user-top']/span[1]/text()").get().strip()
# title = response.xpath("//div[@class='col1 new-style-col1']/h1[@class='article-title']/text()").get().strip()  如果title字符长度大于20，则后面显示...
# datetime = response.xpath("//div[@class='stats']/span[@class='stats-time']/text()").extract_first().strip()
# funny = response.xpath("//span[@class='stats-vote']/i[@class='number']/text()").get().strip()
# content = ",".join(response.xpath("//div[@id='single-next-link']/div[@class='content']/text()").getall())
