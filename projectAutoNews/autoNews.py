import getUrlContentToDB
import filterUrl

if __name__ == '__main__':
    filterInstance = filterUrl.BFScratch()
    filterInstance.readTargetWebsite()
    filterInstance.handleWebsitesDicInfo()

    getUrlContentinstance = getUrlContentToDB.contentToDB('scratchDemo','website')
    # 获取url到数组
    getUrlContentinstance.getUnloadUrlToList()
    # 获取url的content到数组
    getUrlContentinstance.scratchUrlContent()
    # 将url和content保存到指定表中
    getUrlContentinstance.saveInfoToAnotherTables('websiteDetail')
    # 完成上面一步之后，将website中的urlStatus转为1
    getUrlContentinstance.changeUrlStatus()