class BFFileSystem():
    def __init__(self, arg):
        self.arg = arg

    @classmethod
    # 写入数据到指定文件，其中'a'为append的意思就是往后加
    def writeDataToFile(cls, content, fileName):
        with open(fileName,'a') as f:
            f.write(content + '\n')
