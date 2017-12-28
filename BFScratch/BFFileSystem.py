import json
import os
class BFFileSystem():
    def __init__(self, arg):
        self.arg = arg

    @classmethod
    def writeDataToFileAppend(cls, content, filePath):
        """there are many way to write data to file. this is append way meaning
           add text to the file endline

        Args:
            content: message to write to the file
            filePath: the path to find the file

        Returns:
            null
        """
        with open(filePath,'a') as f:
            f.write(content + '\n')


    @classmethod
    def readJsonFolderSavedDic(cls, folderPath):
        """Read the folder document which is json type, return dictionary. if
           document type is not json this method will directly return and print
           message about only support json file

        Args:
            cls: class method default
            folderPath: the path of the folder

        Returns:
            dictionary which saved the folder document information
        """
        # folder dictionary
        folderDic = dict()
        for file in os.listdir(folderPath):
            # judge whether the document is json type
            if ".json" in file:
                fileNameKeyDelSuffix = file[:-5]
                fileDic = json.load(open(folderPath + '/' + file))
                folderDic.update({fileNameKeyDelSuffix: fileDic})
            else:
                print(file + " in " + folderPath + " not be read because only support json type")
        return folderDic


    @classmethod
    def writeDataToFileCover(cls, content, filePath):
        """there are many way to write data to file. this is cover way meaning
           add text to the file covered the previous content

        Args:
            content: message to write to the file
            filePath: the path to find the file

        Returns:
            null
        """
        with open(filePath,'w') as f:
            f.write(content)
