# -*- coding: utf-8 -*-
import re
from lxml import etree
import operator
from BFStringDeal import BFStringDeal

# re文本处理模块
# originalString = "<div>outSideOne<div>inSideOne</div><div>inSideTwo</div></div>"
#
# regxStr = "<div.*</div>"
#
# regx = re.compile(regxStr)
#
# resultArray = regx.findall(originalString)
#
# print(resultArray)



##########################################################
##########################################################

# 网址核心内容判断规则说明：

# github上有很多html解析库，目的在于提取出给定网址的核心内容，这个需求，其实是不能适用于较多场景的
# 本模块聚焦在新闻类的main content提取，和github上其他库相比，优点在于，代码更精简，注释更充分，适用场景更明确
# 打分依据：
#
# 判断一个网址中内容是不是main content，方式多种多样，这里采用p标签判断，text判断结合的方式，其中p标签暂定占比20%，
# text长度占比80%

# etree文本处理模块
originalString = "<div class=\"outsiteone\"><p>p logo</p>outSideOne<div class=\"insideone\">inSideOne</div><div class=\"insidetwo\">inSideTwo</div><div>message<p>haha</p></div></div>"

# rootNode = etree.HTML(originalString).xpath("//div[contains(@class, \"insidetwo\")]")[0].tag

# 存放“候选人”基本信息的字典， key值为在root中的div元素出现的序列号 == value值代表改div元素的string表达
candidataBaseInfoDict = dict()

# 存放“候选人”打分结果的字典，key值为在root中div元素出现的序列号 == value值代表该div元素的打分结果
candidateEvaluateDict = dict()

# 获取文档最底层的xpath node
rootNode = etree.HTML(originalString)

# 存放所有divNODE的列表
divHandleNode = rootNode.xpath("//div")

#####
xxxx = "<div>xxxxxxxxxxx<div>yyyyyyy</div>xxxx</div>"
yyy = BFStringDeal.deleteAllTag(xxxx)

print(yyy)

####

# 处理候选人基本信息
for i in range(0,len(divHandleNode)):
    divHandleText = etree.tostring(divHandleNode[i]).decode("utf-8")
    print(divHandleText)
    # 很多时候，由于div元素过多，所以，我们在这里需要进行一个，最基本判断，如果没有</p>直接没有竞选资格
    if "</p>" in divHandleText:
        print(divHandleText)
        candidataBaseInfoDict.update({i:divHandleText})

# 处理候选人打分结果字典
for key in candidataBaseInfoDict:
    textLengthValue = len(candidataBaseInfoDict[key]) * 2
    candidateEvaluateDict.update({key:textLengthValue})


# 最后我们取出最高分数


# 查看下候选人基本信息
print(candidataBaseInfoDict)

# 查看下候选人的打分情况
print(candidateEvaluateDict)

# 评分系统, 得到最终候选人的node节点位置，基于root
print(max(candidateEvaluateDict.items(), key=operator.itemgetter(1))[0])
