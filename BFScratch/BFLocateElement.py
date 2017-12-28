from lxml import etree
from BFScratch.BFLog import BFLog
class BFLocateElement():
    """BFLocateElement overview

    enter the precise positioning information of the element in the document
    obtained through xpath and output the positioning element content.

    Attributes:
        contentType: dom or json indicate the type of data to be parsed
        analyzingConditions: based on this positioning element
        originalSource: input data source
    """

    def __init__(self, contentType, analyzingConditions, originalSource):
        """init method
        the most basic initialization function. all the args has been explained
        in the overview.
        """
        self.contentType = contentType
        self.analyzingConditions = analyzingConditions
        self.originalSource = originalSource

    def locate(self):
        """the core part of positioning operations

        Args:
            null

        Returns:
            the contents when positioning operation is completed
        """
        if (self.contentType == 'dom'):
            BFLog.bfecho('=== original source ===' + self.originalSource)
            BFLog.bfecho('=== analyzingConditions ===' + self.analyzingConditions)
            # whether analyzingConditions is very accurately
            conditionList = self.analyzingConditions.split('***')
            if len(conditionList) == 1:
                nodeList = etree.HTML(self.originalSource).xpath(self.analyzingConditions)
            else:
                # 这个地方比较难，比较难。。。记住先清空数组，然后在判断是否得到的数据len是不是0
                loopNum = len(conditionList)
                nodeList = list()
                for i in range(loopNum):
                    # 第一次执行这个操作
                    if len(nodeList) == 0:
                        nodeList = etree.HTML(self.originalSource).xpath(conditionList[i])
                    # 非第一次执行该操作
                    else:
                        # 将nodeList缓存起来，然后清空，接下来赋值好用
                        storeList = nodeList
                        nodeList = []
                        for j in range(len(storeList)):
                            resultList = storeList[j].xpath('.' + conditionList[i])
                            # 如果lxml得到的list不是空的话，就向nodeList中添加
                            if len(resultList) > 0:
                                # 循环添加每个list中的item
                                for item in resultList:
                                    nodeList.append(item)

            return nodeList

        elif (self.contentType == 'json'):
            print('use json')
        else:
            print('present only support json and dom analysis')
