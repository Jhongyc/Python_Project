# Author:GaoYuCai
import xml.etree.ElementTree as ET
tree=ET.ElementTree(file="c:\\file1.xml")
root=tree.getroot()
for child_of_root  in root:
    print(child_of_root.tag,child_of_root.attrib)
print(root[0].tag,root[0].text)
for elem in tree.iter(tag="branch"):
    print(elem.tag,elem.attrib)