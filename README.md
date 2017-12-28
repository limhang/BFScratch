# BFScratch

[![PyPI version](https://badge.fury.io/py/BFScratch.svg)](https://badge.fury.io/py/BFScratch)

[view README in English](./README_zh-CN.md)

这是一个处理新闻网站采集的框架，使用python开发。该项目依赖于`lxml`和`requests`，`pymsql`第三方。

---

## BFScratch框架概览
BFScratch框架由以下几个模块组成

* **BFRequest**: 处理url网络请求，返回原始的html文本
* **BFLocateElement**: 输入xpath的定位路径，返回一个xpath的node节点元素
* **BFElementEvaluate**: BFLocateElement可以理解为手动处理元素定位，该模块是自动处理元素定位，这是BFScratch核心模块
* **BFStringDeal**: 该模块主要负责字符串处理
