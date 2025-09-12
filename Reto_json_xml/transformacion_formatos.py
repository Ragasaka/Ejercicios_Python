import xml.etree.ElementTree as ET
import json
import os

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

arch = converter_json_xml()

arch.convert('Ejercicio_json.json')
