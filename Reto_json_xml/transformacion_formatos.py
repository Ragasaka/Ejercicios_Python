import xml.etree.ElementTree as ET
import json
import os

def cast_string_to_number(s: str):
    """
    Receives a string and tries to cast it to int or float.
    Returns the number if possible, otherwise returns None.
    """
    try:
        # Try integer first
        if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
            return int(s)
        
        # Try float
        return float(s)
    except ValueError:
        # Not a number
        return None
    
def cast_to_list(a_string: str):
    if(a_string.startswith['['] and a_string.endswith(']')):
        a_string = a_string.strip(('[',']'))
        return a_string.split(', ')
    else:
        return False

class converter_json_xml():
    def __init__(self):
        pass

    def convert(self,file_name : str):
        if(file_name.endswith('.json')):
            print('Se hará la conversión de json a xml')
            with open(file_name,'r') as file:
                data = json.load(file)
                print(type(data))
                root = ET.Element('data')
                root = self._transform_dicts_xml(root,data)
                tree = ET.ElementTree(root)
                tree.write('a_file.xml')

        elif(file_name.endswith('.xml')):
            print('Se hará la conversión de xml a json')
        else:
            print('Tipo de archivo equivocado, pruebe con un .json o un .xml')

    
    def _create_an_element_xml(self,tag : str, content : any) -> ET.Element:
        new_element = ET.Element(tag)
        if(type(content).__name__ != str):
            new_element.text = str(content)
        else:
            new_element.text = content
        return new_element

    def _transform_dicts_xml(self, base_node: ET.Element, a_dict: dict) -> ET.Element:
        for x in a_dict:
            if (type(a_dict[x]).__name__ != type({'a':'b'}).__name__):
                child_root = self._create_an_element_xml(x,a_dict[x])
                base_node.append(child_root)
            else:
                child_root = ET.Element(x)
                base_node.append(self._transform_dicts_xml(child_root,a_dict[x]))
        return base_node
    
def extract_info_from_xml (trees_root : ET.Element):
    the_dict = {}
    for element in trees_root :
        if(len(element)>0):
            the_dict[element.tag] = extract_info_from_xml(element)
        else: 
            the_dict[element.tag] = element.text
    
    return the_dict



sample_dict = {
    'integer':7,
    'float':12.5,
    'char':'c',
    'comida': {
        'frutas':'manzana',
        'carne':'pollo',
        'vegetales':'lechuga'
    },
    'set':{1,2,3}
}
'''
arch = converter_json_xml()

arch.convert('Ejercicio_json.json')'''


with open('a_file.xml', 'r') as file:
    tree = ET.parse(file)
    root = tree.getroot()

#Base case

the_dict = extract_info_from_xml(root)

print(the_dict['comida'])
print(type(the_dict['comida']))
print(len(root[0]))