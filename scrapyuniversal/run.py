import sys
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

import utils


def run():
    name = sys.argv[1]
    custom_settings = utils.get_config(name)
    spider = custom_settings.get("spider", "universal")
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    update_settings = custom_settings.get('settings')
    if update_settings:
        settings.update(update_settings)
    process = CrawlerProcess(settings)
    # 创建一个spider， spider是爬虫的名称，
    process.crawl(spider, **{"name": name})
    process.start()


if __name__ == '__main__':
    run()
