# 模块的调试等级
class BFLog():
    # class variable
    debugLevel = 0
    def __init__(self, arg):
        self.arg = arg

    @classmethod
    def bfecho(cls, message):
        if cls.debugLevel == 1:
            print(message)
        else:
            pass
