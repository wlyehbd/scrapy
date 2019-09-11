import re
import json
from jsonpath import jsonpath


class Parser:
    def __init__(self, *args, **kwargs):
        self.response = kwargs.get("response")
        self.type = str(kwargs.get("type"))
        self.regex = kwargs.get("regex")

    def parser(self):
        return getattr(self, self.type)()

    """
    css解析器
    """
    def css(self):
        parse_data = [""]
        if self.regex:
            regexs = self.regex.split("&")
            try:
                for i in range(len(regexs)):
                    result = self.response.css(regexs[i].strip()).extract()
                    if result:
                        return result
                return []
            except Exception as e:
                print(e)
        return parse_data

    """
    xpath解析器
    """
    def xpath(self):
        parse_data = [""]
        if self.regex:
            regexs = self.regex.split("&")
            try:
                for i in range(len(regexs)):
                    result = self.response.xpath(regexs[i].strip()).extract()
                    if result:
                        return result
                return []
            except Exception as e:
                print(e)
        return parse_data

    """
    rpath 正则解析器
    """
    def rpath(self):
        text = str(self.response.text)
        parse_data = re.findall(self.regex, text)
        return parse_data

    """
    jpath json解析器
    """
    def jpath(self):
        body = str(self.response.text)  # 可能有乱码问题
        try:
            if isinstance(body, str) or isinstance(body, str):
                body = json.loads(body)
            result = jsonpath(body, self.regex)
        except Exception as e:
            result = []
            print(e)
        if not result:
            result = []
        # 兼容jpath [*] 问题
        data = []
        if "[*]" in self.regex and result:
            for x in result:
                if not isinstance(x, str):
                    data.append(x)
                else:
                    break
            return data
        return result

    """
    resp resp 解析器
    """
    def resp(self, *args, **kwargs):
        r = self.response
        try:
            for i in self.regex.split("."):
                if "##" in i:
                    data = i.split("##")
                    r = getattr(r, data.pop(0))
                    for x in data:
                        r = r.get(x)
                    return [r]
                r = getattr(r, i)
        except Exception as e:
            print(e)
        return [r]