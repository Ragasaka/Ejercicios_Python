the_list = ['a','b','c','d']
the_tuple = ('lunes', 'martes', 'miercoles', 'jueves')
the_set = {'enero', 'febrero', 'marzo', 'abril'}
the_dict = {0:{'Kevin': 'Arroyave', 'Arroyave':'gmail.com'}, 1:'Arroyave', 'age':21, 'sex':'masculino'} 

# Muestra el tipo de estructura que hay

print(f'El tipo de dato de the_list es {type(the_list)}')
print(f'El tipo de dato de the_tuple es {type(the_tuple)}')
print(f'El tipo de dato de the_set es {type(the_set)}')
print(f'El tipo de dato de the_dict es {type(the_dict)} \n')

#Muestra los datos contenidos en cada estructura

print(f'En the_list hay: {the_list}')
print(f'En the_tuple hay: {the_tuple}')
print(f'En the_set hay: {the_set}')
print(f'En the_dict hay: {the_dict} \n')
print(the_dict[0])

#Añade datos

# Listas

print(the_list)

the_list.append('f')
print(the_list)

the_list.insert(len(the_list) - 1, 'e')
print(the_list)

# Sets

print(the_set)

the_set.add('junio')
print(the_set)

the_set.add('mayo')
print(the_set)

# Dicts
print(the_dict)

the_dict['pais'] = 'Colombia'
print(the_dict)

#Actualizacion de datos

# Listas

print('\n')

for i in range (0,len(the_list),1) :
    the_list[i] = chr(ord(the_list[i]) - 32)
else : 
    print(the_list)

# Dicts

the_dict['pais'] = 'Kazajistan'
print(the_dict)

# Eliminar componentes.

# Listas

the_list.remove('A')
print(the_list)
the_list.pop()
print(the_list)
the_list.pop(2)
print(the_list)
the_list.clear()
print(the_list)

# Sets

print(the_set)
the_set.remove('abril')
print(the_set)
the_set.pop()
print(the_set)
the_set.clear()
print(the_set)

# Dicts

print(the_dict)
the_dict.pop(0)
print(the_dict)
the_dict.popitem()
print(the_dict)
del the_dict['sex']
print(the_dict)
the_dict.clear()
print(the_dict)