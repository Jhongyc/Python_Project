# Author:GaoYuCai
import xml.etree.ElementTree as ET
new_xml=ET.Element("personinfolist")
personinfo=ET.SubElement(new_xml,"personifo",attrib={"enrolled":"yes"})
name=ET.SubElement(personinfo,"name")
age=ET.SubElement(personinfo,"age",attrib={"checked":"no"})
sex=ET.SubElement(personinfo,"sex")
age.text="24"
name.text="gaoyucai"
personinfo2=ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
age=ET.SubElement(personinfo,"age")
age.text="19"
et=ET.ElementTree(new_xml)#生成文档对象
et.write("test.xml",encoding='utf-8',xml_declaration=True)
ET.dump(new_xml)#打印生成的格式