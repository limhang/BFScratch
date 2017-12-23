from lxml import etree

class BFLocateElement():
    """BFLocateElement overview

    enter the precise positioning information of the element in the document
    obtained through xpath and output the positioning element content.

    Attributes:
        contentType: dom or json indicate the type of data to be parsed
        analyzingConditions: based on this positioning element
        originalSource: input data source
    """

    def __init__(self, contentType, analyzingConditions, originalSource):
        """init method
        the most basic initialization function. all the args has been explained
        in the overview.
        """
        self.contentType = contentType
        self.analyzingConditions = analyzingConditions
        self.originalSource = originalSource

    def locate(self):
        """the core part of positioning operations

        Args:
            null

        Returns:
            the contents when positioning operation is completed
        """
        if (self.contentType == 'dom'):
            node = etree.HTML(self.originalSource).xpath(self.analyzingConditions)[0]
            return etree.tostring(node).decode("utf-8")
        elif (self.contentType == 'json'):
            print('use json')
        else:
            print('present only support json and dom analysis')
