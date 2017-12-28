# BFStringDeal API Document
处理字符串相关的工具类

---

## 一、常规使用
### 1-1、specialTXT
删除文本中特殊字符`【"\n"】`

```
def specialTXT(cls, text):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| text |需要处理的字符|
|返回值| content |删除特殊字符后的文本|


### 1-2、getAssignContent
按照传入的正则表达式，处理指定字符串，返回处理后的数组
```
def getAssignContent(cls, text, assignContent):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| text |待处理的字符串|
|参数| assignContent |传入的正则表达式字符串|
|返回值| regxList |处理后的数组结果|

## 二、与html有关的字符串操作
### 2-1、deleteAllTag
删除给定文本的所有html标签，<xxx> </xxx>
```
def deleteAllTag(cls, content):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| content |待处理文本内容|
|返回值| backendDelContent |删除了所有html标签的内容|

### 2-2、deleteFrontAndBackendTag
删除头尾tag标签信息  -- 目前还有一点错误，就是删除尾部tag，不一定删除的是最后的
```
def deleteFrontAndBackendTag(cls,content):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| content |待处理文本内容|
|返回值| backendDelContent |删除了前尾标签的内容|


### 2-3、deleteHtmlTag
删除指定的标签，暂时有点问题
```
def deleteHtmlTag(cls, originalTxt):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| originalTxt |需要处理的文本|
|返回值| hasDealTag |处理完毕的文本|




