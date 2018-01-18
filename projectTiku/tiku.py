# 网络请求类，下载url的html文本 # 小程序 - 教师资格证万题库
from BFScratch.BFRequest import BFRequest
import time
import json

# 设定的网址
requestTime = str(time.time()).split('.')[0] + '000'

paperId = '7642223'  # 2011年下半年《小学教育知识与能力》真题

httpsString = "https://api.566.com/minapp/api/question/ImitateExam?t=" + requestTime + "&paperId=" + paperId + "&userExamPaperId=0"

# 初始化网络请求类
bfrequestM = BFRequest(httpsString,'GET')
print(bfrequestM)

print('xx')
# 获取到url的html文本资源
source = bfrequestM.getWebsiteContent()

json_acceptable_string = source.replace("'", "\"")
sourceJson = json.loads(json_acceptable_string)

with open('result.json', 'w') as fp:
    json.dump(sourceJson, fp)  
# 打印获取的内容

print('yy')
