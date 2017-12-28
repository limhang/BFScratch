# BFScratch

[![PyPI version](https://badge.fury.io/py/BFScratch.svg)](https://badge.fury.io/py/BFScratch)

[view README in English](./README_zh-CN.md)

这是一个处理新闻网站采集的框架，使用python开发。该项目依赖于`lxml`和`requests`，`pymsql`第三方。

---

## 一、BFScratch框架概览
BFScratch框架由以下几个模块组成

* **BFRequest**: 处理url网络请求，返回原始的html文本
* **BFLocateElement**: 输入xpath的定位路径，返回一个xpath的node节点元素
* **BFElementEvaluate**: BFLocateElement可以理解为手动处理元素定位，该模块是自动处理元素定位，这是BFScratch核心模块
* **BFStringDeal**: 该模块主要负责字符串处理

## 二、基本使用
### 2-1、开发环境配置
推荐使用`virtualenv`做环境隔离，如果不熟悉python3环境搭建，可以使用虚拟机[vagrant](https://github.com/limhang/centos69)

下载安装`BFScratch`框架
```
pip install BFScratch
```

### 2-2、运用BFScratch框架
最简单的使用代码：

```
# 网络请求类，下载url的html文本
from BFScratch.BFRequest import BFRequest
# 自动定位元素模块，智能匹配文章主体部分
from BFScratch.BFElementEvaluate import BFElementEvaluate

# 设定的网址
htmlSourceEngList = "http://www.chinadaily.com.cn/a/201712/20/WS5a39ce2ea31008cf16da265d.html"
# 初始化网络请求类
bfrequestM = BFRequest(htmlSourceEngList,'GET')
# 获取到url的html文本资源
source = bfrequestM.getWebsiteContent()

####################评分系统模块--使用BFElementEvaluate####################
bfelementEvaluate = BFElementEvaluate(source)
mainContent = bfelementEvaluate.getMainContent()
# 打印获取的内容
print(mainContent)
```

获取到文章的主体内容如下：

```
<div id="Content">
       
      <figure class="image" style="display: table;"> 
 <img src="http://img2.chinadaily.com.cn/images/201712/20/5a39cfcca31008cfb2e7d945.jpeg" data-from="newsroom" data-mimetype="image/jpeg" id="img-5a39cfcca31008cfb2e7d945"> 
 <figcaption style="display: table-caption; caption-side: bottom;">
   Los Angeles Lakers icon Kobe Bryant waves to the crowd at the start of a ceremony at halftime to retire his two jersey numbers, 8 and 24, at Staples Center in Los Angeles, on Dec 18, 2017. [Photo/Agencies] 
 </figcaption> 
</figure> 
<p>LOS ANGELES - Although Kobe Bryant has been asked many times, he still isn't sure who would win a mystical game of one-on-one between the young Kobe in his No 8 Lakers jersey and his older self, who wore No 24.</p> 
<p>"I kind of go back and forth," Bryant said with a sly grin. "But 8 has something that 24 will never, ever, ever have, and that's the ability to grow hair." The Lakers couldn't choose, either. So they honored both eras of Kobe's incredible career.</p> 
<p>In an NBA first, the Lakers on Monday night retired both jersey numbers worn by Bryant, the leading scorer in franchise history.</p> 
<p>Bryant attended the Lakers' game against the Golden State Warriors for a halftime ceremony at Staples Center, which was packed with fans eager to bear witness once again to the beloved superstar scorer. Dozens of Bryant's former teammates showed up, including Shaquille O'Neal and Derek Fisher, along with the Lakers' usual cavalcade of celebrity fans.</p> 
<p>"I feel great," Bryant said after entering Staples Center while pushing a stroller containing Bianka Bella Bryant, his infant daughter. "I'm very proud I get to come here with my family. It feels good as a father to have my family come in and share this."</p> 
<p>Bryant is the 10th player with a retired jersey for the 16-time NBA champion Lakers. His numbers were revealed high on the Staples Center wall, flanking the banner honoring Lakers broadcaster Chick Hearn.</p> 
<p>"It's not about the jerseys that are hanging up there for me," Bryant told the cheering crowd. "It's about the jerseys that were hanging up there before. They inspired me to play the game at a high level."</p> 
<p>Magic Johnson and Lakers owner Jeanie Buss gave brief tributes to Bryant at halftime, with Magic boldly declaring, "We're here to celebrate the greatest who ever wore the purple and gold."</p> 
<p>Buss cleverly explained the reasoning behind the Lakers' decision to hang two jersey numbers for Bryant: "If you separated each of the accomplishments under those numbers, each of those players would qualify for the Hall of Fame."</p> 
<p>"I thank you for staying loyal to the purple and gold and remaining a Laker for life when it might have been easier for you to leave," Buss added.</p> 

    </div>
```

上述打印结果中存在`html`的标签，在[api文档](https://github.com/limhang/BFScratch/tree/master/docs)中有接口去做各种高级操作，包括不限于去标签，去除指定标签，一键排版等等

## 三、高级使用
### 3-1、使用范例
[详细可见github库](https://github.com/limhang/BFScratch)

### 3-2、支持的功能
* 智能爬取新闻类网页，主体内容 ✅
* 爬取xpath导出的模糊条件的node数组 ✅
* 爬取指定(精准)xpath数组 ✅
* 追踪指定网页（主要新闻类）内容是否更新，如果更新，自动拉取，保存数据库 ✅
* 反爬虫机制，集成phantomjs无头浏览器，待更新 🈚️
* log模块日志功能，暴露给外界控制，待更新 🈚️
* 智能爬取新闻主体内容，提供权重配置参数给外界，待更新 🈚️

高级使用功能api接口，[文档有说明](https://github.com/limhang/BFScratch/tree/master/docs)