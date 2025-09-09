import xml.etree.ElementTree as ET
import os

os.chdir("C:\\Users\\karroyave\\OneDrive - ENDAVA\\Documents\\Ejercicio_python\\Ejercicios_Python\\Reto_json_xml")
with open('country_data.xml','r') as file:
    tree = ET.parse(file)
    root = tree.getroot()

print(f'La raíz del archivo xml es: {root.tag}')
print(f'Y el atributo de la raíz del archivo xml es: {root.attrib}')
print(f'El tipo de dato de la raíz del archivo xml es: {type(root)}\n')
print('Los elementos contenidos en este arbol son: \n')

for child in root :
    print(f'{child.tag},{child.attrib}')
print('\n')

print(f'{root[0].attrib}')
print(f'{root[1].attrib}')
print(f'{root[2].attrib}')

print('\n')

print(f'{root[0][0].text}')
print(f'{root[1][0].text}')
print(f'{root[2][0].text}')

print('\n')

print(f'{root[0][1].text}')
print(f'{root[1][1].text}')
print(f'{root[2][1].text}')

print('\n')

print(f'{root[0][2].text}')
print(f'{root[1][2].text}')
print(f'{root[2][2].text}')

print('\n')

print(f'{root[0][3].attrib}')
print(f'{root[1][3].attrib}')
print(f'{root[2][3].attrib}')

print('\n')