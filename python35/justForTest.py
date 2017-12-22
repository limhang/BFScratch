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






#
# #####
# xxxx = "<div>xxxxxxxxxxx<div>yyyyyyy</div>xxxx</div>"
# yyy = BFStringDeal.deleteAllTag(xxxx)
#
# print(yyy)
#
# ####





# 最后我们取出最高分数
