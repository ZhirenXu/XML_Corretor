import xml.etree.ElementTree as ET
import os

#param: xml file, correctDataCombine
def correctXml(*param):
    dataKey = []
    newFileName = ""
    
    #get all file name
    dataKey = param[1].keys()
    for fileName in dataKey:
        if fileName in param[0]:
            #openedXML = open(param[0], 'r+b')
            #find correct tuple contain issue date and page number
            valueForFile = param[1][fileName]
            tree = ET.parse(param[0])
            Xmd_toc = tree.getroot()
            #change issue_date in Xmd_toc
            Xmd_toc.set('ISSUE_DATE', valueForFile[0])
            #change pages_num, doc_date, doc_uid in Meta
            Head_np = Xmd_toc[0]
            Meta = Head_np.find('Meta')
            Meta.set('PAGES_NUMBER', valueForFile[1])
            Meta.set('DOC_DATE', valueForFile[0])
            Meta.set('DOC_UID', "OHI_" + valueForFile[0])
            #output corrected file
            tree.write(param[0])
    #print("\nFile name has no match with any name in csv. Go to next File...")

    return param[0]
