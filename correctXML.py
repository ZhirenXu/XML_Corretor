from functions import Greeting
from functions import SimpleCSV
from functions import AskBypass
from functions import ReadXML
from functions import ReadCSV
from functions import RunProcess
from functions import WriteCSV

def main():
    outFile = ""
    fileIn = ""
    releaseDate = []
    xmlList = []
    xmlListCp = []
    attrValList = []
    tagAttrDict = {}
    fileWithDate = {}
    correctDataCombine = {}
    numOfAttrs = 0

    Greeting.showInfo()
    fileIn = ReadCSV.getCSV()
    correctDataCombine = ReadCSV.getCorrectData(fileIn)
    xmlList = ReadXML.readXML()
    xmlListCp = xmlList.copy()

    while (len(xmlList) > 0):
        print("Processing File: ", xmlList[0], " ......", end = "")
        outFile = RunProcess.correctXml(xmlList.pop(0), correctDataCombine)
        print("Done.")
    print("\nAll files have been corrected.")
    Greeting.sysExit()
    
if __name__ == "__main__":
    main()
