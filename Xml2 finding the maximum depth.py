import xml.etree.ElementTree as etree
maxdepth = -1
def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1
        
    for child in elem:
        depth(child, level + 1)
