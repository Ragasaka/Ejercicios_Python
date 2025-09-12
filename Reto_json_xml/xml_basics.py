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

print(f'{root[0][2].text}', type(root[0][2].text))
print(f'{root[1][2].text}')
print(f'{root[2][2].text}')

print('\n')

print(f'{root[0][3].attrib}')
print(f'{root[1][3].attrib}')
print(f'{root[2][3].attrib}')

print('\n')

#Se creará un nuevo campo dentro del arbol xml creado anteriormente

parser = ET.XMLPullParser(['start', 'end'])
parser.feed('<my_tag>Some text')

a =list(parser.read_events())

print(f'El evento fue {a[0][0]} y el elemento fue {a[0][1]}')

parser.feed(' and more text</my_tag>')

for event, elem in parser.read_events():
    print(event)
    print(elem.tag, 'text=', elem.text)

# Ahora pasaremos por todos los vecinos con un iterador. (funciona de manera recursiva, así se adentra dentro de los arboles y subarboles) 

for neighbors in root.iter('neighbor'): 
    print(neighbors.attrib)

# Sigue una  nueva iteración que consiste en extraer el subarbol iniciado con el tag country para hallar su atributo 
# y el elemento rank

for country in root.findall('country') :
    name = country.get('name')
    rank = country.find('rank').text
    neighbor = country.find('neighbor')
    print(name, rank, neighbor)

# Ahora vamos a modificar el arbol que tenemos de la siguiente forma:
    # 1. Se va a mofidicar el campo rank con el método .text
    # 2. Se a añadir/modificar el atributo de rank con el método .set()
    # 3. No se creará un nuevo hijo de la rama a la que se acceda con .append()

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('update','yes') #Primero nombre de atributo y luego su valor.

tree.write('output.xml') # Esto crea un nuvo archivo .xml sin necesidad de un contexto previo

# Ahora vamos a eliminar un subarbol con el método .remove().

for country in root.findall('country') :
    rank_num = int(country.find('rank').text)
    if rank_num > 50:
        root.remove(country)
    
tree.write('output2.xml')

# Ahora vamos a crear un nuevo arbol con los métodos .element() y .subelement()

a = ET.Element('A') 
b = ET.SubElement(a,'B',{'Level':"1"})
c = ET.SubElement(a,'C',{'Level':"1"})
d = ET.SubElement(c,'D',{'Level':"2"})
second_tree = ET.ElementTree(a)
second_tree.write('output3.xml')


second_root = second_tree.getroot()
second_root[0].text = "Good morning"
second_root[1][0].text = "Good night"
second_root[1].text = "Good afternoon"

second_tree.write('output4.xml',encoding='utf-8',xml_declaration=True,)

