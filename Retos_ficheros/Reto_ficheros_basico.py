import os

os.chdir('C:\\Users\\karroyave\\OneDrive - ENDAVA\\Documents')

try:
    with open('Ragasaka.txt', 'w') as f :
        f.write('Información básica\n')
        print('creando archivo')
except FileExistsError as e:
    print(f'{type(e).__name__}: el archivos ya existe')
except PermissionError as e:
    print(f'{type(e).__name__}: no se tiene permisos suficientes para crear el archivo')
except Exception as e:
    print(f'A ocurrido un error inesperado {type(e).__name__}: {e}')
else:
    with open('Ragasaka.txt', 'a') as f:
        f.write('Nombre: Kevin Arroyave Arroyave\n')
        f.write('Edad: 22\n')
        f.write('Lenguaje favorito: Python\n')
    print('Ya se creó el archivo')
finally :
    '''with open('Ragasaka.txt', 'r') as f:
        content = f.readline()
    print(f'El contenido de archivo era:\n{content}')'''
    '''print(f'El contenido de archivo era:\n')
    with open('Ragasaka.txt', 'r') as f:
        for content in f:
            print(content)'''
    with open('Ragasaka.txt', 'r') as f:
        content = f.readlines()
    print(f'El contenido era:\n{content}')
    for i in content:
        print(i)
    
b = True

while (b):
    c = input('Pon q para salir: ')
    match c:
        case 'q':
            b = False
        case 'Q':
            b = False

print('fin de programa')

os.remove(os.path.join(os.getcwd(),'Ragasaka.txt'))