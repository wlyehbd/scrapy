"""
@Author  : hanbingde@zhugefang.com
@Time    : 2019/6/3
@Desc    :

"""


class SpiderInit:
    def __init__(self, **kwargs):
        self.config = {}
        self.type = kwargs.get("type", "")
        self.rules = kwargs.get("rules", "")

    def getStartUrl(self):
        return self.rules.fields_rules.get("start_url", [])
