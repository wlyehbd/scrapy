"""
@Author  : hanbingde@zhugefang.com
@Time    : 2019/5/28
@Desc    :

"""

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from spider.spiders.dmoz_spider import DmozSpider
import importlib
import sys

class Blackwidow:
    def __init__(self, **kwargs):
        self.s_type = kwargs.get("s_type")
        self.channel = kwargs.get("channel")
        self.settings = Settings()

        self.blackwidow = self.__getBlackwidowRules__()
        self.__setSetting__()

        # 注册中间件
        self.__setMiddlewares__()

        # 注册pip
        self.__setPipelines__()

        self.process = CrawlerProcess(self.settings)
        self.__setSpider__()

        self.process.start()

    def __setSpider__(self):
        dmoz = DmozSpider
        self.process.crawl(
            dmoz,
            type=self.s_type,
            rules=self.blackwidow
        )

    def __getBlackwidowRules__(self):
        blackwidow_posterity_path = (
            "spider.rules.test"
        )

        blackwidow_posterity_json = importlib.import_module(
            blackwidow_posterity_path
        )
        return blackwidow_posterity_json

    def __setSetting__(self):
        pass

    def __setMiddlewares__(self):
        pass

    def __setPipelines__(self):
        pipelines = {
            "seeds": "spider.pipelines.SeedsPipeline",
            "details": "spider.pipelines.DetailsPipeline",
        }
        self.settings.set("ITEM_PIPELINES", {pipelines.get(self.s_type): 300})


if __name__ == '__main__':
    channel = "test"
    s_type = "seeds"
    if len(sys.argv) > 2:
        channel = sys.argv[1]
        s_type = sys.argv[2]

    Blackwidow(
        s_type=s_type,
        channel=channel
    )
