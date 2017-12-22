import re
class BFElementEvaluate():
    def __init__(self, htmlContent, section):
        self.section = section
        self.htmlContent = htmlContent

    def getXpathLocation(self):
        if (self.section == "article"):
            # 如果我们需要获取文章中，最主体核心的部分


        else:
            print("present only support article part")
