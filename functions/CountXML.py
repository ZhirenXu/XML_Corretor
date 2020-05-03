import os

## get number of xml files under directory and fill a list that contains all xml file names
# @param    xmlList
#           a list contain xml file names 
# @return   xmlCounter
#           how many xml file in this directory
# @update   xmlList

def countXML(xmlList):
    currentDir = ""
    xmlCounter = 0
    fileList = []
    
    currentDir = os.getcwd()
    fileList = os.listdir()
    print("\nCurrent Directory: ", currentDir, "\n")
    print("Files under this directory: ")
    for file in fileList:
        print(file)
        if(".xml" in file):
            xmlCounter += 1
            xmlList.append(file)
    print("\n\nTotal number of file: ", len(fileList), end = "")
    return xmlCounter
