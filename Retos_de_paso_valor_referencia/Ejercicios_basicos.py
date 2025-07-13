
# Ejemplo de paso por valor

def suma_cualquier_cosa (num1, num2) :
    num1 = num1 + 1
    num2 = num2 - 1
    print(f'num1 es {num1}')
    print(f'num2 es {num2}')

def cambia_string (word) :
    word = word + ' !'
    print(word)

def global_suma_cualquier_cosa () :
    global sx, sy
    sx = sx + 1
    sy = sy - 1
    print(f'sx es {sx}')
    print(f'sy es {sy}')

def global_cambia_string () :
    global ss
    ss = ss + ' !'
    print(ss)

def suma_corriente (a, b) :
    return (a + b)

def cambia_list (a_list) :
    a_list[0] = 'hola'

def inserta_fruta (a_set, new_fruit) :
    a_set.add(new_fruit)

def limpia_lista (a_list) :
    a_list = []
    
def quita_elemento (variable) :
    variable.pop()

def expande_dict (a_dict) :
    a_dict['name'] = 'Kevin'
    a_dict['surname'] = 'Arroyave'
    a_dict['age'] = 22

def modifica_dict (a_dict) :
    a_dict['surname'] = 'Arroyave Arroyave'

def borra_dict (a_dict) :
    del a_dict['age']
    del a_dict

# Con enteros
x = 2
y = 3
suma_cualquier_cosa (x, y) 

print(f'x es {x}')
print(f'y es {y}')

# Con flotantes
x = 2.7
y = 3.6
suma_cualquier_cosa (x, y) 

print(f'x es {x}')
print(f'y es {y}')

# Con complejos 

x = 2 + 3j
y = 3 - 9j
suma_cualquier_cosa (x, y) 

print(f'x es {x}')
print(f'y es {y}')

# Con string

s = 'Hola'
cambia_string(s)

print(f'Realmente era {s}')

'''

 Ahora se va a hacer un paso por referencia con variables básicas por medio de la palabra clave global
 dentro de una funciones.

 Una variable básica en Python es global por defecto para la lectura; si se quiere modificar, entonces hay 
 usar la keyword global dentro de la función para hacer lo que llamamos el paso por referencia o volverla global
 en el sentido global de la palabra

 '''

# Primero con enteros 

sx = 1
sy = 3

print('Llama la función global_suma_cualquier_cosa')
global_suma_cualquier_cosa()

print('Dentro del prgrama principal')

print(f'sx es {sx}')
print(f'sx es {sy}')

sx = 1
sy = 3

print('Llama la función global_suma_cualquier_cosa')
global_suma_cualquier_cosa()

print('Dentro del prgrama principal')

print(f'sx es {sx}')
print(f'sx es {sy}')

#Luego flotantes

sx = 178.5
sy = 78575.53

print('Llama la función global_suma_cualquier_cosa')
global_suma_cualquier_cosa()

print('Dentro del programa principal')

print(f'sx es {sx}')
print(f'sx es {sy}')

#Después complejos

sx = 178.5 + 3454365.889j
sy = 78575.53 -7456.5345645j

print('Llama la función global_suma_cualquier_cosa')
global_suma_cualquier_cosa()

print('Dentro del programa principal')

print(f'sx es {sx}')
print(f'sx es {sy}')

#Y por último strings

ss = 'Hola Mundo'


print('Llama la función global_cambia_string')
global_cambia_string()

print('Dentro del programa principal')

print(f'ss es {ss}')

'''

El uso de la palabra clave return ¿ Cuenta como un paso por valor ?
Inicialmente creo que no ,por que la palabra clave return devuelve 
un valor o dato como consecuencia de la ejecución de una función,
si se usa una de las variables usadas como argumento como varibale de destino para contener el resultado
de la función y a efectos prácticos sería como si hubieramos hecho un paso por referencia.

'''
x = 120
y = -100

print(f'la variable x es {x}')
print(f'la variable y es {y}')

print('Se llama a la función suma_corriente')
x = suma_corriente(x, y)

print('Ahora')

print(f'la variable x es {x}')
print(f'la variable y es {y}')

'''
Ahora es tiempo de hablar de los tipo de datos especiales o estructuras de datos, 
los cuales en un primer momento son las listas, las tuplas, los sets y las diccionarios. 

En la consulta que he realizado hasta el momento se supone que estos tipos de datos al ser suministrados 
como argumentos en una función son pasados por referencia

'''

simple_list = ['Hola']

print(f'simple_list es {simple_list}')
print('Se llama a la funcio cambia_string')

cambia_list (simple_list)

print(f'Simple_list en el programa principal es {simple_list}')

simple_list.append('sengundo elemento')

simple_list[0] = 'Hola'

print(f'simple_list es {simple_list}')
print('Se llama a la funcio cambia_string')

cambia_list (simple_list)

print(f'Simple_list en el programa principal es {simple_list}')

print('Se llama a la funcio limpia_lista')

limpia_lista(simple_list)

print(f'Simple_list en el programa principal es {simple_list}')

print(f'Se llama a la función quita_elemento')

quita_elemento(simple_list)

print(f'simple_list en el programa principal es {simple_list}')

# Probemos con sets

frutas_set = {'naranja', 'mango', 'papaya'}

print(f'frutas_set es {frutas_set}')
print('Se llama a la función inserta_fruta')
inserta_fruta (frutas_set, 'fresas')

print(f'frutas_set en el programa principal es {frutas_set}')

print('Se llama a la funcio limpia_lista')

limpia_lista(frutas_set)

print(f'frutas_set en el programa principal es {frutas_set}')

print(f'Se llama a la función quita_elemento')

quita_elemento(frutas_set)

print(f'frutas_set en el programa principal es {frutas_set}')

#Pruebas en diccionarios

my_dict = {}

print(f'my_dict es {my_dict}')
print('Se llama a la función expande_dict')

expande_dict(my_dict)

print(f'my_dict en el programa principal es {my_dict}')

print('Se llama a la función modifica_dict')

modifica_dict(my_dict)

print(f'my_dict en el programa principal es {my_dict}')

print('Se llama a la función borra_dict ')

borra_dict(my_dict)

print(f'my_dict en el programa principal es {my_dict}')

# un ejemplo extra

list_a = [10,20,54]
list_b = [43,90]

print(f'list_a es {list_a}')
print(f'list_b es {list_b}')
print('Ahora no')

list_b = list_a

print(f'list_a es {list_a}')
print(f'list_b es {list_b}')

print('Ahora menos')
list_b[1] = 90

print(f'list_a es {list_a}')
print(f'list_b es {list_b}')

# Conclusiones

'''
Las variables que corresponden a tipos de datos como los son los int, float, complex, char y string,
por defectos se pasa por valor. Esto es, entregarle una copia del valor de la variable a la función.

Una variable dentro del programa principal se considera global para unicamente efectos de letura por defecto,
no obstante, es posible habilitar la posibilidad de escitura de la variable por medio de la palabra clave
global dentro de la función que la quiere usar como tal, claro está, esta palabra clave debe ir acompañada a
su derecha del nombre que tiene la variable en el programa principal. Con esta keyword un variable de tipo de
datos básico podría pasarse por referencia a efectos prácticos.

El uso de palabra clve return al final de la función no obliga a un paso por referencia.

'''