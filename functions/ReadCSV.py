import csv
import sys

def getCSV():
    csv = ""
    attrsList = []
    releaseNo = []
    
    print("Please enter a csv file that want to use for correcting data in xml.")
    print("Attributes should all be put in the first row, like a header. In the header, each cell should only has one attribute.")
    print("File name(with .csv): ", end = "")
    csv = input()

    return csv
## read first row of @csv and output its contents as a list
# @param    csv
#           input csv
# @return   attrs
#           a list content all cell contents
def readAttr(csvFile):
    attrs = []
    
    with open(csvFile, encoding="utf-8-sig") as inFile:
        try:
            csvReader = csv.reader(inFile, delimiter=',')
            for row in csvReader:
                attrs = row
                break
            inFile.close()
        except:
            print("Fail to open file. Please check again. Press any key to exit. ")
            key = input()
            sys.exit()
    return attrs

def getAllRows(csvReader):
    listOfRow = []
    for row in csvReader:
        listOfRow.append(row)
    #delete header
    listOfRow.pop(0)
    
    return listOfRow

def getReleaseNo(rowList):
    releaseNo = []
    
    for row in rowList:
        releaseNo.append(row[1])

    return releaseNo

#this is the key for combineDataDict
def getReleaseDate(releaseNo):
    releaseDate = []

    for release in releaseNo:
        #stripe the data from each release no
        data = release[8 : 18]
        releaseDate.append(data)
    return releaseDate

def getIssueDate(rowList):
    issueDate = []

    for row in rowList:
        issueDate.append(row[10])

    return issueDate


def getPageNumber(rowList):
    pageNumber = []

    for row in rowList:
        pageNumber.append(row[14])

    return pageNumber

#**param: input file, attrib0, attrib1
def getCorrectData(*param):
    combinedData = {}
    releaseNo = []
    #value of the key. key:[val0, val1]
    value = []
    #key of the combinedData
    releaseDate = []
    #value0 of key
    issueDate = []
    #value1 of the key
    pageNumber = []
    
    with open(param[0], encoding="utf-8-sig") as inFile:
        try:
            csvReader = csv.reader(inFile, delimiter=',')
        except:
            print("Fail to open ", param[0], ". Please check again. Press any key to exit. ")
            key = input()
            sys.exit()
        rowData = getAllRows(csvReader)
    inFile.close()
    releaseNo = getReleaseNo(rowData)
    releaseDate = getReleaseDate(releaseNo)
    issueDate = getIssueDate(rowData)
    pageNumber = getPageNumber(rowData)
    
    for date in releaseDate:
        value.append(issueDate.pop(0))
        value.append(pageNumber.pop(0))
        combinedData[date] = value
        value = []
    
    return combinedData
