from functions import ReadCSV

## read attrs from input csv file
# @return    attrsList
#           a list contains all desired attributes
def readAttr():
    csv = ""
    attrsList = []
    releaseNo = []
    
    print("Please enter a csv file that want to use for correcting data in xml.")
    print("Attributes should all be put in the first row, like a header. In the header, each cell should only has one attribute.")
    print("File name(with .csv): ", end = "")
    csv = input()
    attrsList = ReadCSV.readAttr(csv)
    return attrsList
