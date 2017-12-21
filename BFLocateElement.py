from lxml import etree


# 元素定位获取模块
# 这个模块将要细分为2个组成部分
# section one -- 定位解析字符串 【dom】
# section two -- 定位解析json  【json】
class BFLocateElement():
    def __init__(self, contentType, content, originalSource):
        # 支持2种类型，一是json解析；二是纯text的html文本(requests.text获取的)
        self.type = contentType
        # 用户在浏览器中，通过xpath helper获取到的定位元素的表达
        self.content = content
        # BFRequest模块中传入的text解析文本
        self.originalSource = originalSource

    # 返回给外界解析后的数据
    def locate(self):
        # 传入的是dom文本的情况
        if (self.type == 'dom'):
            node = etree.HTML(self.originalSource).xpath(self.content)[0]
            return etree.tostring(node).decode("utf-8")
        elif (self.type == 'json'):
            print('use json')
        else:
            print('present only support json and dom analysis')
