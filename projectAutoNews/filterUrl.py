# 一。本地调试使用
# loadDependency是依赖导入文件，是需要最先引入的，如果有其他文件夹的库，请在该模块导入
# import loadDependency
# # 网络请求模块
# from BFRequest import BFRequest
# # 手动定位模块
# from BFLocateElement import BFLocateElement
# # 自动定位元素模块
# from BFElementEvaluate import BFElementEvaluate
# # 文件处理模块，读写等多种操作
# from BFFileSystem import BFFileSystem
# # 数据库操作模块
# from BFDBOperate import BFDBOperate

# 二。pip list BFScratch使用
from BFScratch.BFRequest import BFRequest
from BFScratch.BFLocateElement import BFLocateElement
from BFScratch.BFElementEvaluate import BFElementEvaluate
from BFScratch.BFFileSystem import BFFileSystem
from BFScratch.BFDBOperate import BFDBOperate


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
        print(dic)
        print(filePath)
        handleInstance = scratchWebsiteNewContent(dic,filePath)
        urlList = handleInstance.compareContent()
        print(urlList)
        if len(urlList) > 0:
            # 使用scratchDemo数据库，建2个表一个是网址和内容url和是否需要更新判断关联的表；一个是内容url+maincontent+时间 的这种表

            # CREATE TABLE `website` (
            #     `id` int(10) NOT NULL AUTO_INCREMENT,
            #     `originalUrl` varchar(255) COLLATE utf8_bin NOT NULL,
            #     `contentUrl` varchar(255) COLLATE utf8_bin NOT NULL,
            #     `urlStatus` boolean not null default 0,
            #     PRIMARY KEY (`id`)
            # ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
            # AUTO_INCREMENT=1 ;

            # CREATE TABLE `websiteDetail` (
            #     `id` int(10) NOT NULL AUTO_INCREMENT,
            #     `contentUrl` varchar(255) COLLATE utf8_bin NOT NULL,
            #     `time` varchar(100) COLLATE utf8_bin NOT NULL,
            #     `mainContent` varchar(10240) COLLATE utf8_bin NOT NULL,
            #     PRIMARY KEY (`id`)
            # ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
            # AUTO_INCREMENT=1 ;
            for num in range(0,len(urlList)):
                dbBase = BFDBOperate('scratchDemo','9981aa','root','localhost')
                sqli = "INSERT INTO `website` (`originalUrl`, `contentUrl`) VALUES (%s, %s)"
                info = (dic['url'], urlList[num])
                dbBase.insertDB(sqli, info)

            # 我们先建立第一个表，完成操作之后，在处理第二个表

        else:
            print("this time has no url to update")



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
        print(compareNew)


        # 比较现在的内容和之前存储的内容是否一致
        if compareNew == self.dic["oldCompareContent"]:
            print("do not scratch noting change")
            return ''
        else:
            print("begin scratch ====")
            urlList = self.contentChangeScratchUrl()
            # 将新的字典转化为json，存到filePath中
            self.dic.update({"oldCompareContent":compareNew})
            BFFileSystem.writeDataToFileCover(json.dumps(self.dic),self.filePath)
            return urlList

    # 如果内容有改变，我们将拉取url网址到urlScratch池子
    def contentChangeScratchUrl(self):
        # 这里我们拉取5个url
        # 从json中获取资源定位
        positionIdentify = self.dic["sourcePosition"] # 使用xpath helper获取
        # 获取指定内容
        bflocationM = BFLocateElement('dom', positionIdentify, self.originalContent)
        positionNode = bflocationM.locate()
        # 保存没有重复的前5个，使用text和oldCompareContent比较
        urlList = list()
        for index in range(0,5):
            if positionNode[index].text == self.dic["oldCompareContent"]:
                break
            else:
                urlList.append(positionNode[index].attrib['href'])
        return urlList



# if __name__ == '__main__':
#     instance = BFScratch()
#     instance.readTargetWebsite()
#     instance.handleWebsitesDicInfo()
