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

print('En un lugar de la Mancha cuyo nombre no quiero acordarme')