from functions import CountXML

## read all xml from current directory and report result
# @return   xmlList
#           a list contain all xml files need to be processed
def readXML():
    xmlList = []
    xmlCounter = 0
    
    xmlCounter = CountXML.countXML(xmlList)
    print("    Total number of xml: ", xmlCounter, "\n")

    return xmlList
