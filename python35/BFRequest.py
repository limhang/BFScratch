# -*- coding: utf-8 -*-
import requests

# 网络请求类
class BFRequest():
    # 构造函数 == 接收参数网址
    def __init__(self, url, method):
        self.url = url
        self.method = method
    # 预设请求头
    def preSetHeader(self,header):
        self.header = header

    # 开始获取原始网页内容
    def getWebsiteContent(self):
        # 如果是get请求
        if (self.method == "GET"):
            # 如果没有设置header,通过hasattr判断
            if (hasattr(self,'header')):
                websiteOriginalContent = requests.get(self.url,headers=self.header).content.decode('utf-8')
                return websiteOriginalContent

            else:
                # 获取抓取到的原始网页
                # websiteOriginalContent = requests.get(self.url).content.decode('utf-8')
                websiteOriginalContent = requests.get(self.url).content.decode('utf-8')
                # 这里还必须有异常捕获模块

                return websiteOriginalContent
