from functions import GetTagAttr

## parse xml file and get all tag-attri tuples
# @param    tree
#           parsed xml file
# @return   tagAttr
#           a dict contain tag and its attribute
def parseXML(tree):
    tagAttr = {}
    
    tagAttr = GetTagAttr.getTagAttr(tree)
    
    return tagAttr
