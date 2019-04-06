# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..utils import get_config
from ..rules import rules
from .. import items


class UniversalSpider(CrawlSpider):
    name = 'universal'
    def __init__(self, name, *args, **kwargs):
        config = get_config(name)
        # self.rules 必须在调用父类的__init__方法前赋值，否则self.rules会赋值失败。因为父类的__init__方法会直接对rules进行处理，形成self._rules，在执行时是调用self._rules，而不是调用self.rules，所以如果self.rules在调用父类的__init__方法后赋值，则不会将self.rules的值处理到self._rules中。
        self.rules = rules.get(config.get("rules"))
        self.file_name = name
        self.config = config
        self.start_urls = config.get("start_urls")
        self.allowed_domains = config.get("allowed_domains")
        super(UniversalSpider,self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = self.config.get("item")
        if item:
            # cls = item.get("class"))()
            cls = getattr(items, item.get("class"))()
            loader = getattr(items, item.get("loader"))(cls, response=response)
            attrs = item.get("attrs")
            for key, value in attrs.items():
                for extractor in value:
                    if extractor.get("method") == "xpath":
                        loader.add_xpath(key, *extractor.get("args"), **{"re": extractor.get("re")})
                    elif extractor.get("method") == "css":
                        loader.add_css(key, *extractor.get("args"), **{"re": extractor.get("re")})
                    elif extractor.get("method") == "value":
                        loader.add_value(key, *extractor.get("args"), **{"re": extractor.get("re")})
                    else:
                        loader.add_value(key, getattr(response, *extractor.get("args")))
            yield loader.load_item()
"""
        loader = ChinaLoader(item=NewsItem(), response=response)
        loader.add_xpath("title", "//h1[@id='chan_newsTitle']/text()")
        loader.add_xpath("datetime", "//div[@id='chan_newsInfo']/text()", re=r"(\d+-\d+-\d+\s\d+:\d+:\d+)")
        loader.add_xpath("source", "//div[@id='chan_newsInfo']/text()", re=r"来源：(.*)")
        loader.add_xpath("content", "//div[@id='chan_newsDetail']//text()")
        loader.add_value("url", response.url)
        loader.add_value("website", "中华网")
        yield loader.load_item()
        """
"""
class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['http://tech.china.com/articles/']

    rules = (
        # Rule(link_extractor, callback=None, cb_kwargs=None, follow=None)
        # link_extractor是LinkExtractor对象。
        Rule(LinkExtractor(allow=r'article\/.*\/.*\.html', restrict_xpaths="//div[@id='left_side']/div[@class='con_item']/div[@class='conL']"),callback='parse_item'),
        # Rule(LinkExtractor(restrict_xpaths="//div[@id='pageStyle']/a[contains(., '下一页')]")),
    )

    def parse_item(self, response):
        loader = ChinaLoader(item=NewsItem(), response=response)
        loader.add_xpath("title", "//h1[@id='chan_newsTitle']/text()")
        loader.add_xpath("datetime", "//div[@id='chan_newsInfo']/text()", re=r"(\d+-\d+-\d+\s\d+:\d+:\d+)")
        loader.add_xpath("source", "//div[@id='chan_newsInfo']/text()", re=r"来源：(.*)")
        loader.add_xpath("content", "//div[@id='chan_newsDetail']//text()")
        loader.add_value("url", response.url)
        loader.add_value("website", "中华网")
        yield loader.load_item()


        
        title = response.xpath("//h1[@id='chan_newsTitle']/text()")
        url = response.url
        datetime =  response.xpath("//div[@id='chan_newsInfo']/text()").re_first(r"\d+-\d+-\d+\s\d+:\d+:\d+")
        source = response.xpath("//div[@id='chan_newsInfo']/text()").re_first(r"来源：(.*)").strip()
        # div中存放文章的所有内容，使用extract()提取所有文本，然后使用''.join()连接成字符串
        content = "".join(response.xpath("//div[@id='chan_newsDetail']//text()").extract()).strip()

        item = NewsItem()
        item["title"] = title
        item["url"] = url
        item["datetime"] = datetime
        item["source"] = source
        item["website"] = "中华网"
        item["content"] = content
        
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
"""