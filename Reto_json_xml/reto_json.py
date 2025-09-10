import os
import json

FILENAME = 'Ejercicio_json.json'
data = {
    'name':'Kevin Arroyave Arroyave',
    'age':22,
    'birthday':'2003-07-10',
    'languages':['Python', 'C']
}

with open(FILENAME, 'w') as file:
    json.dump(data,file,indent=4)

print('Ya se creó el archivo.json\n')

with open(FILENAME, 'r') as file:
    saved_data = json.load(file)

print(f'El contenido del .json era:\n{saved_data}\n\nSu tipo de dato al final es {type(saved_data)}')

os.remove(FILENAME)
