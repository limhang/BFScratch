# 一。本地调试使用
# loadDependency是依赖导入文件，是需要最先引入的，如果有其他文件夹的库，请在该模块导入
# import loadDependency
# # 数据库操作模块
# from BFDBOperate import BFDBOperate
# # 网络请求类，下载url的html文本
# from BFRequest import BFRequest
# # 自动定位元素模块，智能匹配文章主体部分
# from BFElementEvaluate import BFElementEvaluate

# 二。pip list BFScratch调试使用
from BFScratch.BFDBOperate import BFDBOperate
from BFScratch.BFRequest import BFRequest
from BFScratch.BFElementEvaluate import BFElementEvaluate


import time;  # 引入time模块

class contentToDB():
    """docstring for contentToDB."""
    def __init__(self,dbName,tableName):
        self.urlList = list()
        self.urlContentList = list()
        # 指定某个数据库
        self.dbName = dbName;
        # 指定某个表
        self.tableName = tableName

    # 选出未更新的网址到urlList数组
    def getUnloadUrlToList(self):
        dbBase = BFDBOperate(self.dbName,'9981aa','root','localhost')
        sqli = "SELECT * FROM " + self.tableName + " WHERE `urlStatus`=%s"
        info = ('0')
        urlSource = dbBase.selectData(sqli, info)
        for index in range(0,len(urlSource)):
            self.urlList.append(urlSource[index]['contentUrl'])
            
    # 依据urlList中的网址，爬取内容存储到urlContentList数组中
    def scratchUrlContent(self):
        for index in range(0,len(self.urlList)):
            # 设定的网址
            htmlSourceEngList = self.urlList[index]
            # 初始化网络请求类
            bfrequestM = BFRequest(htmlSourceEngList,'GET')
            # 获取到url的html文本资源
            source = bfrequestM.getWebsiteContent()

            ####################评分系统模块--使用BFElementEvaluate####################
            bfelementEvaluate = BFElementEvaluate(source)
            mainContent = bfelementEvaluate.getMainContent()
            self.urlContentList.append(mainContent)

    # 将urlList中存储的网址内容爬取到，存到websiteDetail表中
    def saveInfoToAnotherTables(self, tableName):
        for index in range(0,len(self.urlList)):
            dbBase = BFDBOperate(self.dbName,'9981aa','root','localhost')
            sqli = "INSERT INTO " + tableName + " (`mainContent`, `contentUrl`, `time`) VALUES (%s, %s, %s)"
            info = (self.urlContentList[index], self.urlList[index], time.time())
            dbBase.insertDB(sqli, info)


    # 更改website中update为1
    def changeUrlStatus(self):
        for index in range(0,len(self.urlList)):
            dbBase = BFDBOperate(self.dbName,'9981aa','root','localhost')
            sqli = "UPDATE " + self.tableName + " SET `urlStatus`=%s WHERE `contentUrl`=%s"
            info = ('1', self.urlList[index])
            dbBase.updateDB(sqli, info)


# if __name__ == "__main__":
#     instance = contentToDB('scratchDemo','website')
#     # 获取url到数组
#     instance.getUnloadUrlToList()
#     # 获取url的content到数组
#     instance.scratchUrlContent()
#     # 将url和content保存到指定表中
#     instance.saveInfoToAnotherTables('websiteDetail')
#     # 完成上面一步之后，将website中的urlStatus转为1
#     instance.changeUrlStatus()
