import sys

## match attributes with their tag and find it in parsed xml, return attri value
# @param    isBypassed
#           a bool value indicates if error is ignored
# @param    desiredAttr
#           a list contain attributes client want
# @param    tagAttrDict
#           a dict contain specific tag and all attrs of these tag.
#           DesiredAttr is gurantee to be in this dict
# @return   attribValueList
#           a list for all attrib values required
def getAttr(isBypassed, desiredAttr, tagAttrDict):
    attrValue = ""
    attribValueList = []
    
    for key in tagAttrDict.keys():
        attribTuplesDict = tagAttrDict[key]
        for attr in desiredAttr:
            if (attr in attribTuplesDict):
                attrValue = attribTuplesDict[attr]
                attribValueList.append(attrValue)
    if(len(attribValueList) == 0 and (not isBypassed)):
        print("Could not find any keywords in this xml! \nPress enter to ignore once. Press Q to exit.")
        key = input()
        if (key == "Q" or key == "q"):
            sys.exit()
    elif(len(attribValueList) == 0 and isBypassed):
        print("Could not find any keywords in this xml. Bypassed")
    else:
        print("Complete")
    return attribValueList
