#Función capitalize pone la primera letra en mayusculas
print('hola'.capitalize(), '\n')
''' 
Función center, centra la cadena de carateres en la longitud definida en el prime argunmento
si la cadena a centrar no llena toda la longitud especificada, entonces se pueden rellenar los espacios
sobrante con el caracter que se quiera

'''
print('Pithon'.center(len('Python') + 4, '+'))
'''
Función count retorna la cantidad de veces que aparece una cadena especifica 
dentro del rango que se le halla seleccionado al string,
si no sele indica un rango entonces analizará todo el string


'''
string = 'hola hola hola hola'
print(string.count('hola'))
print(string.count('hola',0, 4))
print(string.count('hola',4))

'''

La función encode te devuelve el string proporcionado en sus bytes

'''
print('Python'.encode())
print(type('Python'.encode()))

'''
Endswitch da True or False su en el string analizado termina con
el sufijo o sufijos considerados (en caso de se varios sufijos
hay que ponerlos en una lista)

'''

print('fotos.zip')
print('fotos.zip'.endswith('.zip'))

print('fotos.zip tiene todas las fotos de un viaje')
print('fotos.zip tiene todas las fotos de un viaje'.endswith('.zip'))

print('fotos.zip tiene todas las fotos de un viaje')
print('fotos.zip tiene todas las fotos de un viaje'.endswith(('.zip', 'viaje')))

print('fotos.zip tiene todas las fotos de un viaje')
print('fotos.zip tiene todas las fotos de un viaje'.endswith('.zip',0, 9))

'''
la funcion expandtabs busca los caracteres \t y los reemplaza por la cantidad 
de espacio que se le especifique, eso si respentando los saltos de 
linea y los retorno a inicio

'''

print('Hola\tMundo\n'*2)
print(('Hola\tMundo\n'*2).expandtabs(1))

'''

La función find retona el indice de inicio o menor en donde se 
puede encontrar elsubstyring que se le especifique a la función.
Se puede hacer más especifica la busqueda si se le da un intervalo a 
la función despues del substring, los extremos de subintervalo son algo opcional.

'''
cadena = 'En un lugar de la Mancha cuyo nombre no quiero acordarme'
print('En un lugar de la Mancha cuyo nombre no quiero acordarme')
print('En un lugar de la Mancha cuyo nombre no quiero acordarme'.find('mancha'))
print('En un lugar de la Mancha cuyo nombre no quiero acordarme'.find('Mancha'))
print(cadena[18:18 + len('Mancha')])

'''
Format es una función que generar un nuevo string apartir de uno en el cual se le podian insertar
elementos particulares, esto estos elementos se encuentra dentro de un par de llaves. cuando hay varios
elementos a reemplazar dentro del string original estos dentr del comando pueden  colocarse de forma posicional
o por medio de keyword argumentes

'''
pi = 3.1416
euler = 2.71828
print('El valor de pi es {0} y es el de e es {1}'.format(pi,euler))
print('El valor de pi es {pimpinela} y es el de e es {Euler}'.format(Euler = euler,pimpinela = pi))

'''
Forma_map funciona como forma pero se aplica idealmento con diccionarios

'''
listt = {'name':['Ivan', 'Samuel'], 'age':[32, 53]}

print('{name[0]} tiene {age[0]} años'.format_map(listt))
print('{name[1]} tiene {age[1]} años'.format_map(listt))

'''
La función join retorna una cadena de caracteres que es el resutado de las cadenas de caracteres que 
se le sumunistraron como argumento (es bueno pasarlas como una lista) poniendo entre cadena y cadena 
el string para llmar este método

'''
print(' toca '.join(('Ivan', 'pito')))


'''
lstrip retorna un string sin los caracteres que se pasaron como arguemento en forma de string,
estos caracteres debe de esta al inicio de la cadena para ser removidos.

'''
cadena = 'Esta es una cadena de carecteres a la que le quitaremos las vocales'

print(cadena)
print(cadena.lstrip('Esta '))

'''
Partition toma una cadena de carateres y un substring para retonar tres elementos, lo que había antes del
substring, el substring, y lo que hay despues del substring, todo dentro de una tupla

'''
print(cadena.partition('carecteres'))

'''
Removeprefix elimina unicamente el prefijo que se le indicque y no las combinaciones de caracteres que
se contegan el el prefijo inidicado.

'''
print('The llama')
print('The llama'.removeprefix('The'))

'''
Removesuffix hace lo mismo que la función anterior pero con los sufijos

'''
print('The tenacious D')
print('The tenacious D'.removesuffix('D'))


'''
Replace como su nombre lo indica reemplaza los carcateres que se le indiquen, pero, también se da la opción 
de especificar cuandos reemplazos se puede hacer desde el inicio del string

'''

cadena = 'Quien sera maestro'
print(cadena)
cadena = cadena.replace('a','i').replace('e', 'i').replace('o', 'i')
print(cadena + ',','care palo') #Jajaja

'''
Split te divide la cadena de carecteres en las partes que se le indique cada que en ella se presente un
substring que se le especifique. Si no se especifica el número de divisiones, entonces va a separar la cadena
cada que se presente el substring divisor. En particular el objeto de retorno es una lista

'''
cadena = 'Platano, manzana, pera, naranja, uva, mango, banana, sandia'
print(cadena.replace(', ',' y ',3))
cadena = cadena.replace(', ',' y ')
a_list = cadena.split(' y ')
print(a_list)
print(cadena.split(' y ', 2))
print(cadena.rsplit(' y ', 2))

# Nota: cuando por lo general un metodo empieza por r muy posiblemente hace lo que su contraparte pero
# de inicio a fin, si hay contra parte claro está.

cadena = 'Hola'
a_list = list(cadena)
print(a_list)
print(type(a_list))
n = cadena[::-1]
print(n)
