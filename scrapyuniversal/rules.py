from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


rules = {
    "china": (
        # https://tech.china.com/article/20190404/20190404266905.html
        Rule(LinkExtractor(allow=r"article\/.*\/.*\.html", restrict_xpaths=r"//div[@id='left_side']//div[@class='conL']"), callback="parse_item"),
        # Rule(LinkExtractor(restrict_xpaths=r"//div[@id='pageStyle']/a[contains(., '下一页')]"))
    ),
    "qsbk":(
        Rule(LinkExtractor(allow=r"\/article\/.*", restrict_xpaths=r"//div[@class='article block untagged mb15 typs_long']"), callback="parse_item"),
        Rule(LinkExtractor(restrict_xpaths="//ul[@class='pagination']/li[contains(., '下一页')]"))
    )
}
