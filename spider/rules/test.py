"""
@Author  : hanbingde@zhugefang.com
@Time    : 2019/5/28
@Desc    :

"""
fields_rules = {
    "start_url": ["http://doc.scrapy.org/en/latest/_static/selectors-sample1.html",
                  "http://doc.scrapy.org/en/latest/_static/selectors-sample1.html"],
    "fields_rules": {
        "title": {
            "field": "title",
            "depict": "标题",
            "status": True,
            "type": "",
            "select": "xpath",
            "deep": True,
            "regex": "//a/text()",
        },
    }

}
