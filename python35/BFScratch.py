# loadDependency是依赖导入文件，是需要最先引入的，如果有其他文件夹的库，请在该模块导入
import loadDependency
# 网络请求模块
from BFRequest import BFRequest
# 手动定位模块
from BFLocateElement import BFLocateElement
# 自动定位元素模块
from BFElementEvaluate import BFElementEvaluate
# 文件处理模块，读写等多种操作
from BFFileSystem import BFFileSystem
# 字符串处理模块，大多是类方法
from BFStringDeal import BFStringDeal

# system loadDependency
import os
import json

class BFScratch():
    def __init__(self):
        # self.arg = arg
        # 存放每个网址提供的所有信息
        self.inputSource = dict()
        self.originalContent = str()
    def readTargetWebsite(self):
        ####################文件读写系统--使用BFFileSystem####################
        self.inputSource = BFFileSystem.readJsonFolderSavedDic(os.getcwd() + '/' + 'targetWebsite')

    # 扫描target文件夹，处理里面每一个json文件
    def handleWebsitesDicInfo(self):
        # 循环遍历处理每一个网址
        for k,v in self.inputSource.items():
            # 这里开始针对每一个网址处理
            filePath = os.getcwd() + '/' + 'targetWebsite' + '/' + k + '.json'
            self.handleWebsiteDetail(v,filePath)

    # 这里类似集装箱，将要包含多种不同情况处理，每一个处理都是一个小函数
    def handleWebsiteDetail(self,dic,filePath):
        # 通过该函数获取到网页的原始信息
        handleInstance = scratchWebsiteNewContent(dic,filePath)
        handleInstance.compareContent()


    # 获取给定网址的核心内容--也就是article main content
    # def getWebsiteMainContent(self):
    #     # ####################评分系统模块--使用BFElementEvaluate####################
    #     bfelementEvaluate = BFElementEvaluate(self.originalContent)
    #     mainContent = bfelementEvaluate.getMainContent()



# 这个类是业务类，处理爬最新网页的需求
class scratchWebsiteNewContent():
    def __init__(self, dic, filePath):
        self.dic = dic
        self.filePath = filePath
        self.getOriginalContent()

    # 获取给定网址的内容
    def getOriginalContent(self):
        # ####################网络请求部分--使用BFRequest####################
        bfrequestM = BFRequest(self.dic["url"],'GET')
        # 获取到原始的网址内容
        self.originalContent = bfrequestM.getWebsiteContent()


    # 存储比较内容信息（通过它，判断是否进行爬取操作）
    def compareContent(self):
        ###################元素定位模块--使用BFLocateElement####################
        # 从json中获取定位元素
        positionIdentify = self.dic["IndexPosition"] # 使用xpath helper获取
        # 获取指定内容
        bflocationM = BFLocateElement('dom', positionIdentify, self.originalContent)
        positionNode = bflocationM.locate()
        compareNew = positionNode[0].text
        # 比较现在的内容和之前存储的内容是否一致
        if compareNew == self.dic["oldCompareContent"]:
            print("do not scratch noting change")
        else:
            print("begin scratch ====")
            self.contentChangeScratchUrl()
        # 不管比较的内容是否发生变化，我们都需要更新比较元素到字典中
        self.dic.update({"oldCompareContent":compareNew})
        # 将新的字典转化为json，存到filePath中
        BFFileSystem.writeDataToFileCover(json.dumps(self.dic),self.filePath)


    # 如果内容有改变，我们将拉取url网址到urlScratch池子
    def contentChangeScratchUrl(self):
        # 这里我们拉取5个url
        # 从json中获取资源定位
        positionIdentify = self.dic["sourcePosition"] # 使用xpath helper获取
        # 获取指定内容
        bflocationM = BFLocateElement('dom', positionIdentify, self.originalContent)
        positionNode = bflocationM.locate()
        url = positionNode[2].attrib['href']
        print(url)



if __name__ == '__main__':
    instance = BFScratch()
    instance.readTargetWebsite()
    instance.handleWebsitesDicInfo()



# # 输出给外界xpathSource -- 已经选择好的预期文本
#

# # 输出给外界xpathSource -- 已经选择好的预期文本
#
#
#
# ####################html文本处理部分--使用BFStringDeal####################
# # 去除\n等无效字符
# dealOne = BFStringDeal.specialTXT(mainContent)
# # 设置，自认为合理的文档排序 -- 每一个网站都可以自定义该处正则表达式
# elementList = BFStringDeal.getAssignContent(dealOne,"<p*?>.*?</p>|<img.*?/>|<span.*?>.*?</span>")
# for item in elementList:
#     # print(BFStringDeal.deleteHtmlTag(item))
#
#     # 写入文件
#     BFFileSystem.writeDataToFile(BFStringDeal.deleteHtmlTag(item),'demo.txt')
# # 预期给外界一个合理的元素列表
#
# ####################文件操作部分--使用BFFileSystem####################
