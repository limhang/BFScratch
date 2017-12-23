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

# 使用网址初始化类
# 设置请求头
# test = BFRequest('https://www.reuters.com/article/us-northkorea-missiles/south-korea-says-any-delay-in-military-drills-depends-on-north-koreas-behavior-idUSKBN1EE0FK','GET')
# headers = {
# 'Host':'www.lagou.com',
# 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
# 'Cookie':'user_trace_token=20170208130109-9aaa0404-edbb-11e6-8f61-5254005c3644; LGUID=20170208130109-9aaa0719-edbb-11e6-8f61-5254005c3644; JSESSIONID=F3F361CEED0ACD3F17112753569325C6; _putrc=00C6A03A01332BEB; login=true; unick=%E6%9D%8E%E6%98%8E%E8%88%AA; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=152; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_iOS%3Fpx%3Ddefault%26city%3D%25E6%25B7%25B1%25E5%259C%25B3; _gat=1; TG-TRACK-CODE=index_navigation; SEARCH_ID=4d90963f818446059da0cbf0bdf0b2ba; index_location_city=%E5%B9%BF%E5%B7%9E; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1488005231,1488419706,1488419773,1488504600; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1488510382; _ga=GA1.2.372407027.1486530069; LGSID=20170303104240-11e969ec-ffbb-11e6-a9fb-525400f775ce; LGRID=20170303110621-6110009b-ffbe-11e6-918d-5254005c3644',
# 'Referer':'https://www.lagou.com/jobs/list_php?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput='
# }



####################网络请求部分--使用BFRequest####################
htmlSourceEngList = "http://www.chinadaily.com.cn/a/201712/20/WS5a39ce2ea31008cf16da265d.html"
htmlSourceHangBlog = "http://blog.coderhelper.cn/%E7%BD%91%E7%BB%9C%E6%98%AF%E6%80%8E%E6%A0%B7%E8%BF%9E%E6%8E%A5%E7%9A%84%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0.html"
htmlSourceCailiao = "http://www.runoob.com/python/python-files-io.html"
htmlSourceruanyifeng = "http://www.ruanyifeng.com/blog/2017/12/image-and-wave-filters.html"
bfrequestM = BFRequest(htmlSourceruanyifeng,'GET')
source = bfrequestM.getWebsiteContent()
# 输出给外界source -- html文本

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
    BFFileSystem.writeDataToFile(BFStringDeal.deleteHtmlTag(item),'demo.txt')
# 预期给外界一个合理的元素列表

####################文件操作部分--使用BFFileSystem####################
