import xml.etree.ElementTree as ET
import os

FILENAME = 'Ejercicio_xml.xml'
ROOT_NAME = 'Personal_data'
data = {
    'name':'Kevin Arroyave Arroyave',
    'age':22,
    'birthday':'2003-07-10',
    'languages':['Python', 'C']
}

root = ET.Element(ROOT_NAME)

for x in data :
    y = ET.SubElement(root,x)
    if type(data[x]).__name__ != 'str':
        data[x] = str(data[x])
    y.text = data[x]
    

tree = ET.ElementTree(root)

tree.write(FILENAME)

os.remove(FILENAME)
