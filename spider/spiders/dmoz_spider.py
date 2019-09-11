import scrapy
from spider.common.parser import Parser
from spider.cores.SpiderInit import SpiderInit


class BlackwidowBasicSpider:
    def __init__(self, *args, **kwargs):
        self.config = SpiderInit(**kwargs)

        self.rules = kwargs.get("rules")
        self.type = kwargs.get("type")

    def parse(self, response):
        item = {}
        for i, k in self.rules.fields_rules.get("fields_rules").items():
            res = Parser(
                response=response,
                regex=k.get("regex"),
                type=k.get("select")
            ).parser()
            item[i] = res
        return item


class DmozSpider(BlackwidowBasicSpider, scrapy.Spider):
    def start_requests(self):
        startUrl = self.config.getStartUrl()
        for url_info in startUrl:
            yield self.make_requests_from_url(url_info)

