# BFLocateElement API Document
处理html文本中，元素定位问题，支持xpath插件模糊定位，无需精准指定lxml的node数组的index，返回满足输入条件的node数组。json其他文本，暂时未支持。

---

## 一、BFLocateElement类初始化
使用该模块，需要先实例化BFLocateElement类
```
def __init__(self, contentType, analyzingConditions, originalSource):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| contentType |处理文本的类型，暂时只支持dom|
|参数| analyzingConditions |xpath提取条件，可使用浏览器xpath插件|
|参数| originalSource |待提取文本|
|返回值| null |null|


## 二、元素定位，返回定位信息

```
def locate(self):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| null |null|
|返回值| nodeList |获取定位到的node数组|
