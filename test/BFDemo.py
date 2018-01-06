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

import os

####################网络请求部分--使用BFRequest####################
htmlSourceEngList = "http://www.chinadaily.com.cn/a/201712/20/WS5a39ce2ea31008cf16da265d.html"
htmlSourceHangBlog = "http://blog.coderhelper.cn/%E7%BD%91%E7%BB%9C%E6%98%AF%E6%80%8E%E6%A0%B7%E8%BF%9E%E6%8E%A5%E7%9A%84%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0.html"
htmlSourceCailiao = "http://www.runoob.com/python/python-files-io.html"
htmlSourceruanyifeng = "http://www.ruanyifeng.com/blog/2017/12/image-and-wave-filters.html"
bfrequestM = BFRequest(htmlSourceruanyifeng,'GET')
source = bfrequestM.getWebsiteContent()
# 输出给外界source -- html文本

####################文件读写系统--使用BFFileSystem####################
dic = BFFileSystem.readJsonFolderSavedDic(os.getcwd() + '/' + 'targetWebsite')
print(dic)

####################元素定位模块--使用BFLocateElement####################
# content = "//div[@class='main_art'][1]/div[@class='picshow']/div[@id='Content']"  # 使用xpath helper获取
# bflocationM = BFLocateElement('dom',content,source)
# xpathSource = bflocationM.locate()
# 输出给外界xpathSource -- 已经选择好的预期文本

####################评分系统模块--使用BFElementEvaluate####################
bfelementEvaluate = BFElementEvaluate(source)
mainContent = bfelementEvaluate.getMainContent()
# 输出给外界xpathSource -- 已经选择好的预期文本



####################html文本处理部分--使用BFStringDeal####################
# 去除\n等无效字符
dealOne = BFStringDeal.specialTXT(mainContent)
# 设置，自认为合理的文档排序 -- 每一个网站都可以自定义该处正则表达式
elementList = BFStringDeal.getAssignContent(dealOne,"<p*?>.*?</p>|<img.*?/>|<span.*?>.*?</span>")
for item in elementList:
    # print(BFStringDeal.deleteHtmlTag(item))

    # 写入文件
    BFFileSystem.writeDataToFileAppend(BFStringDeal.deleteHtmlTag(item),'demo.txt')
# 预期给外界一个合理的元素列表

####################文件操作部分--使用BFFileSystem####################
