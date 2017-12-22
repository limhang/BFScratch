# BFScratch

[中文查看](./README_zh-CN.md)

newspaper collected framework used python. BFScratch dependence `lxml` `re` ,thanks those genius
---

## BFScratch overview
BFScratch include several modules.

* **BFRequest**: handle URL request，return original HTML text
* **BFLocateElement**: if you input the specify xpath location, this module will return Element located.
* **BFElementEvaluate**: BFLocateElement seemed to be manual work for specify element location. you can also use this module that handle element location automatically. this is BFScratch central part.
* **BFStringDeal**: this module work for string regx tasks.
