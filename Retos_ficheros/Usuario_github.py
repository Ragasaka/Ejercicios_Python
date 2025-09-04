import os

DIR = "C:Users\\karroyave\\OneDrive - ENDAVA\\Desktop"
FILE_NAME = "Ragasaka.txt"

os.chdir(DIR)

with open(FILE_NAME, 'w') as f:
    f.write('Nombre: Kevin\nEdad: 22\n,Lenguaje principal: Python')

with open(FILE_NAME,'r') as f:
    contenido = f.read()

print('\n'+contenido+'\n')

os.remove(FILE_NAME)