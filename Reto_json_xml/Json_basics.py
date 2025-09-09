#Ejemplos básicos del maenjo de la librería por defecto
#de Python para Python

import json

emp = '{"id":"09","name":"Nitin","department":"Finance"}' #Un archivo Json interpretaría este str como un objeto que viene a comportarse cómo un set de python aunque su sintaxis parezca a la de un diccionario
print('This is JSON', type(emp)) #A fin de cuentos Json es un formato para guardar datos del web en un archivo de texto.

print('\nNow convert from JSON to Python')

#Convert string to Python dict
d = json.loads(emp)
print('\nConverted to Python',type(d),'\n')
print(d)

print('\nNow convert to JSON forma')

print('This is Python', type(d))
with open('Filemon_y_sus_amigos.txt', 'w') as file:
    d = json.dump(d,file,indent=1)

    print('\nNow this is JSON', type(d))
    print(f'\n{d}')

example_2 = {'name':'Filemon', 'age':27, "salary": 3100}

second_json = json.dumps(example_2, indent=4)

print(f'El segundo json creado es: \n{second_json}\n')
print(f'Y su nuevo tipo de dato es {type(second_json).__name__}')

with open("ejercicio_datos_json.txt",'w') as file:
    json.dump(['Hola','mundo','!','En dict'], file,indent=4)
    json.dump(('Hola','mundo','!', 'En tupla'), file,indent=4)
    json.dump(123,file,indent=4)
    json.dump(123.123,file,indent=4)
    json.dump(True,file,indent=4)
    json.dump(False,file,indent=4)
    json.dump(None,file,indent=4)

var = {
    'subjects': {
        'Math':85,
        'Physics':90
    }
}

with open('Sample.txt','w') as file:
    json.dump(var,file,indent=4)

