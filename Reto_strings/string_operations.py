#Función capitalize pone la primera letra en mayusculas
print('hola'.capitalize(), '\n')
''' 
Función center, centra la cadena de carateres en la longitud definida en el prime argunmento
si la cadena a centrar no llena toda la longitud especificada, entonces se pueden rellenar los espacios
sobrante con el caracter que se quiera

'''
print('Pithon'.center(len('Pithon') + 4, '+'))
'''
Función count retorna la cantidad de veces que aparece una cadena especifica 
dentro del rango que se le halla seleccionado al string,
si no sele indica un rango entonces analizará todo el string


'''
string = 'hola hola hola hola'
print(string.count('hola'))
print(string.count('hola',0, 4))
print(string.count('hola',4))