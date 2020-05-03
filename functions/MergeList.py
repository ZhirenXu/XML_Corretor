##merge result from single xml file to a total list that contains list of
# required attrib values
#
# @param    desiredAttr
#           a list contain desired attributes for a single xml
# @param    resultList
#           a list contain list of required attrib values
# @param    numOfAttrs
#           count how many attrs clients want; use for merge
# @update   resultList
# @update   attrValList

def mergeList(desiredAttr, resultList, numOfAttrs):
    i = 0
    
    while (i < numOfAttrs):
        resultList[i].append(attrValList.pop(0))
        i += 1
        
