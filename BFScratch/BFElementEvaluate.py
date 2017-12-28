import re
from BFScratch.BFStringDeal import BFStringDeal
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

        # 处理候选人基本信息 ---- 【初选】
        for i in range(0,len(divHandleNode)):
            divHandleText = etree.tostring(divHandleNode[i]).decode("utf-8")
            # print(divHandleText)
            # 很多时候，由于div元素过多，所以，我们在这里需要进行一个，最基本判断，如果没有</p>直接没有竞选资格
            if "</p>" in divHandleText:
                # print(divHandleText)
                self.candidataBaseInfoDict.update({i:divHandleText})

        # text文本判断 ---- 【第一轮竞选】
        for key in self.candidataBaseInfoDict:
            removeTagContent = BFStringDeal.deleteAllTag(self.candidataBaseInfoDict[key])
            # 如果文本大于400，直接满分
            if len(removeTagContent) > 400:
                self.candidateEvaluateDict.update({key:70})
            else:
                textLengthValue = len(removeTagContent) / 400 * 100 * 0.7
                self.candidateEvaluateDict.update({key:textLengthValue})

        # node子节点数量判断 ---- 【第二轮竞选】
        for key in self.candidataBaseInfoDict:
            nodeChildrenNum = len(divHandleNode[key].getchildren())
            # 如果子node的个数大于10，那么直接满分
            originalValue = self.candidateEvaluateDict[key]
            if nodeChildrenNum > 9:
                self.candidateEvaluateDict.update({key:(originalValue + 15)})
            else:
                renewValue = nodeChildrenNum * 10 * 0.15
                self.candidateEvaluateDict.update({key:(originalValue + renewValue)})

        # p标签数量判断 ---- 【第三轮竞选】
        for key in self.candidataBaseInfoDict:
            # 如果子node的个数大于10，那么直接满分
            NodePNum = len(divHandleNode[key].xpath("./p"))
            originalValue = self.candidateEvaluateDict[key]
            if NodePNum > 5:
                self.candidateEvaluateDict.update({key:(originalValue + 15)})
            else:
                renewValue = NodePNum * 100 / 6 * 0.15
                self.candidateEvaluateDict.update({key:(originalValue + renewValue)})

        # 查看下候选人基本信息
        # print(self.candidataBaseInfoDict)

        # 查看下候选人的打分情况
        # print(self.candidateEvaluateDict)

        # 评分系统, 得到最终候选人的node节点位置，基于root
        contentNodeNumber = max(self.candidateEvaluateDict.items(), key=operator.itemgetter(1))[0]

        handleResult = etree.tostring(divHandleNode[contentNodeNumber],encoding="unicode", pretty_print=True, method="html")
        # print(handleResult)
        return handleResult
