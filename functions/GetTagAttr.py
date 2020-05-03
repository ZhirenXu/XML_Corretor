import xml.etree.ElementTree as ET

## find all Attrs for <Xmd_toc> and <Meta>
# @param    tree
#           parsed xml document
# @return   tagAttrDict
#           a dict, key is tag, value are all its attrs
def getTagAttr(tree):
    tagAttrDict = {}
    
    Xmd_toc = tree.getroot()
    tagAttrDict[Xmd_toc.tag] = Xmd_toc.attrib
    Head_np = Xmd_toc[0]
    Meta = Head_np[0]
    tagAttrDict[Meta.tag]= Meta.attrib

    return tagAttrDict    
