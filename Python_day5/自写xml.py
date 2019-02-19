# Author:GaoYuCai
import xml.etree.ElementTree as ET
G=ET.Element("GAo")
name=ET.SubElement(G,"name",attrib={"enrolled":"yes"})
age=ET.SubElement(name,"age",attrib={"checked":"no"})
sex=ET.SubElement(name,"sex")
age.text='19'
sex.text="nan"
name.text="Gao"
et=ET.ElementTree(G)
et.write("test1.xml",encoding="utf-8",xml_declaration=True)
ET.dump(G)