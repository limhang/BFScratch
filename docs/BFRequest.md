# BFRequest API Document
处理网络请求，返回得到的html文本信息

---

## 一、BFRequest类初始化
设置网址和请求方法
```
def __init__(self, url, method):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| url |待处理的网址|
|参数| method |请求的方法，常见的get，post|
|返回值| null |null|


## 二、设置请求头【可选】
设置请求头，有些网址，有做请求头限制，这个是可选的
```
def preSetHeader(self,header):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| header |待传入的请求头|
|返回值| null |null|

可供参考的例子:
```
headers = {
'Host':'www.lagou.com',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
'Cookie':'user_trace_token=20170208130109-9aaa0404-edbb-11e6-8f61-5254005c3644; LGUID=20170208130109-9aaa0719-edbb-11e6-8f61-5254005c3644; JSESSIONID=F3F361CEED0ACD3F17112753569325C6; _putrc=00C6A03A01332BEB; login=true; unick=%E6%9D%8E%E6%98%8E%E8%88%AA; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=152; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_iOS%3Fpx%3Ddefault%26city%3D%25E6%25B7%25B1%25E5%259C%25B3; _gat=1; TG-TRACK-CODE=index_navigation; SEARCH_ID=4d90963f818446059da0cbf0bdf0b2ba; index_location_city=%E5%B9%BF%E5%B7%9E; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1488005231,1488419706,1488419773,1488504600; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1488510382; _ga=GA1.2.372407027.1486530069; LGSID=20170303104240-11e969ec-ffbb-11e6-a9fb-525400f775ce; LGRID=20170303110621-6110009b-ffbe-11e6-918d-5254005c3644',
'Referer':'https://www.lagou.com/jobs/list_php?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput='
}
```

## 三、获取网址内容方法
### 2-1、getWebsiteContent
通过该方法获取网址内容文本
```
def getWebsiteContent(self):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| null |null|
|返回值| websiteOriginalContent |网址的html文本|


