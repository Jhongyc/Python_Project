# Author:GaoYuCai
import  xml.etree.ElementTree as ET
tree=ET.ElementTree("test1.html")
root=tree.getroot()
for node in root.find("name"):
    age=int(node.find("age").text)+1
    age.text=str(age)
tree.write("test1.xml")