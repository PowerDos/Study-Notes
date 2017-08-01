# XML处理模块
import xml.etree.ElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()
print(root)
print(root.tag)

# 遍历xml文档
print("####################遍历xml文档####################")
# attrib是遍历属性
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        if not i.attrib:
            print(i.tag, i.text)
        else:
            print(i.tag, i.text, i.attrib)

# 只遍历year 节点
print("####################只遍历year 节点####################")
for node in root.iter('year'):
    print(node.tag, node.text)

# 修改
print("####################修改XML####################")
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updated", "yes")
# tree.write("test.xml")

#删除node
print("####################删除XML####################")
# for country in root.findall('country'):
#    rank = int(country.find('rank').text)
#    if rank > 50:
#      root.remove(country)
#tree.write('output.xml')

# 新建XML文件
print("####################新建XML文件####################")
new_xml = ET.Element("namelist")
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name = ET.SubElement(personinfo,"name")
name.text= "Gavin"
age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})
sex = ET.SubElement(personinfo, "sex")
age.text = '33'
sex.text = 'male'
personinfo2 = ET.SubElement(new_xml, "personinfo2", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2,"name")
name.text= "Gavin"
age = ET.SubElement(personinfo2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("xmltest.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式