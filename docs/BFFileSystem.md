# BFFileSystem API Document
负责处理文件相关操作，包括不限于指定文件/文件夹读写操作

---

## 一、写相关操作
### 1-1、writeDataToFileAppend
写入数据到指定文件，如果文件存在且有内容，那么在最后一行新增要写入的数据
```
def writeDataToFileAppend(cls, content, filePath):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| content |需要写入到文件的内容|
|参数| filePath |写入文件的路径加文件名|
|返回值| null |null|


### 1-2、writeDataToFileCover
写入数据到指定文件，如果文件存在且有内容，覆盖掉文件的内容
```
def writeDataToFileCover(cls, content, filePath):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| content |需要写入到文件的内容|
|参数| filePath |写入文件的路径加文件名|
|返回值| null |null|

## 二、读相关操作
### 2-1、readJsonFolderSavedDic
读取指定文件夹中所有的json文件，以json文件名作为`key`值，内容作为`value`，处理该文件夹中所有json文件，返回一个大字典。
```
def readJsonFolderSavedDic(cls, folderPath):
```

|IO|名称|说明|
| :--- | :----: | :----: |
|参数| folderPath |需要读取的文件夹路径|
|返回值| folderDic |所有json文件最终转化的一个大字典|


