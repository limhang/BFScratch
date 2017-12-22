import re
from BFStringDeal import BFStringDeal
from lxml import etree
import operator

class BFElementEvaluate():
    def __init__(self, htmlContent):
        # 外界传入的htmlContent
        self.htmlContent = htmlContent
        # 存放“候选人”基本信息的字典， key值为在root中的div元素出现的序列号 == value值代表改div元素的string表达
        self.candidataBaseInfoDict = dict()
        # 存放“候选人”打分结果的字典，key值为在root中div元素出现的序列号 == value值代表该div元素的打分结果
        self.candidateEvaluateDict = dict()
        # 获取文档最底层的xpath node
        self.rootNode = etree.HTML(htmlContent)
    # 获取文章主体部分内容
    def getMainContent(self):
        # 初始化。实例变量的值
        self.candidataBaseInfoDict = {}
        self.candidateEvaluateDict = {}

        # 存放所有divNODE的列表 -- 基本上所有mainContent一定是div结构
        divHandleNode = self.rootNode.xpath("//div")

        # 处理候选人基本信息
        for i in range(0,len(divHandleNode)):
            divHandleText = etree.tostring(divHandleNode[i]).decode("utf-8")
            # print(divHandleText)
            # 很多时候，由于div元素过多，所以，我们在这里需要进行一个，最基本判断，如果没有</p>直接没有竞选资格
            if "</p>" in divHandleText:
                # print(divHandleText)
                self.candidataBaseInfoDict.update({i:divHandleText})


        # 处理候选人打分结果字典
        for key in self.candidataBaseInfoDict:
            textLengthValue = len(self.candidataBaseInfoDict[key]) * 2
            self.candidateEvaluateDict.update({key:textLengthValue})


        # 查看下候选人基本信息
        # print(self.candidataBaseInfoDict)

        # 查看下候选人的打分情况
        # print(self.candidateEvaluateDict)

        # 评分系统, 得到最终候选人的node节点位置，基于root
        contentNodeNumber = max(self.candidateEvaluateDict.items(), key=operator.itemgetter(1))[0]

        print(etree.tostring(divHandleNode[contentNodeNumber]).decode("utf-8"))
