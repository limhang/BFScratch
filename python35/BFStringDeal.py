# 工具类，字符串处理
import re

class BFStringDeal(object):
    def __init__(self,arg):
        self.arg = arg

    @classmethod
    # 删除垃圾字符 -- 比如：\n
    def specialTXT(cls, text):
        return text.replace("\n", "")

    @classmethod
    # 正则表达式处理，字符串
    def getAssignContent(cls, text, assignContent):
        # 获取正则表达式实例，其中assignContent为外界传入的表达式值
        regx = re.compile(assignContent)
        return regx.findall(text)

    @classmethod
    # 删除html前尾部标签，传入值为单个标签 p or h1
    # 常用tag标签有【h1,h2,h3,h4,h5,a,span,img,p】 -- 其中img需要单独处理下
    def deleteHtmlTag(cls, originalTxt):
        # 外部输入进来，tag，在此处合成 -- 例如 tag-h1 output <h1.*?>.*?</h1>
        tagCollection = ['p','h1','h2','h3','h4','a','p','span']
        for tag in tagCollection:
            tagCompelete = "<" + tag + ".*?" + '>|' + '</' + tag + '>'
            regx = re.compile(tagCompelete)
            hasDealTag = regx.sub("",originalTxt)
            # 删除h1，h2，p中含有标签a的情况
            if "</a>" in hasDealTag:
                tagCompelete = "<" + 'a' + ".*?" + '>|' + '</' + 'a' + '>'
                regx = re.compile(tagCompelete)
                hasDealTag = regx.sub("",originalTxt)
            # 删除h1，h2，p中含有标签span的情况
            if "</span>" in hasDealTag:
                tagCompelete = "<" + 'span' + ".*?" + '>|' + '</' + 'span' + '>'
                regx = re.compile(tagCompelete)
                hasDealTag = regx.sub("",originalTxt)

            # 含有img的情况以后处理


            return hasDealTag

    @classmethod
    # 删除头尾tag标签信息  -- 目前还有一点错误，就是删除尾部tag，不一定删除的是最后的
    # eg:传入<div class="fasdfd">something so many <div>ssss</div></div>
    #    得到something so many <div>ssss</div>
    def deleteFrontAndBackendTag(cls,content):
        # 删除tag前缀
        frontTag = "<.*?>"
        regxFront = re.compile(frontTag)
        frontDelContent = regxFront.sub("",content,1)

        # 删除tag后缀 == 这里只是需要删除</xx>就可，不一定会删除最后一个
        backendTag = "</.*?>"
        regxBack = re.compile(backendTag)
        backendDelContent = regxBack.sub("",frontDelContent,1)
        return backendDelContent



    @classmethod
    # 删除给定文本的所有tag
    # eg:传入<div class="fasdfd">something so many <div>ssss</div></div>
    #    得到something so many ssss
    def deleteAllTag(cls, content):
        frontTag = "<.*?>"
        regxFront = re.compile(frontTag)
        frontDelContent = regxFront.sub("",content)

        backendTag = "</.*?>"
        regxBack = re.compile(backendTag)
        backendDelContent = regxBack.sub("",frontDelContent)
        return backendDelContent
