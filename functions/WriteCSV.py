import sys
import csv
from itertools import zip_longest

# write attributes and attributes' value into csv file
# @param    xml
#           a list contains all input xml files
# @param    attrList
#           a list contains name of scraped attributes
# @param    resultList
#           a list contain lists of attributes' value
# @param    outputFile
#           output File pointed by user
def writeCSV(xml, attrList, resultList, outputFile):
    print("Writing attribute values into ", outputFile, "...")
    try:
        outFile = open(outputFile, 'w', encoding = 'utf8', newline='')
        csvWriter = csv.writer(outFile)
        csvWriter.writerow(attrList)
        for singleFileResult in resultList:
            #add input file name to the list about to write
            singleFileResult.insert(0, xml.pop(0))
            csvWriter.writerow(singleFileResult)
        print("Complete!")
        outFile.close()
    except:
        print("Fail to write csv!")
