import os
'''
with open('Primer_archivo.txt', 'w') as f :
    c = f.write('Este\nes\nmi\nprimer\narchivo')

print(f'Se escribieron {c} caracteres')
'''

new_path = 'C:\\Users\\karroyave\\OneDrive - ENDAVA\\Desktop\\Carpeta_creada_con_python'


try :

    os.makedirs(new_path)
    print(f'El directorio {new_path} a sido creado exitosamente')

except FileExistsError as e:
    
    print(f'{type(e).__name__}: El directorio {new_path} ya existe')
    
except PermissionError as e :

    print(f'''{type(e).__name__}: No cuentas los permisos necesarios para crear el 
          directorio {new_path}''' )
    
except Exception as e :

    print(f'Oops... A ocurrido un error\n{type(e).__name__}: {e}')

finally:

    os.chdir(new_path)

    with open('El hechicero.txt','w') as f :
        c = f.write('Y sus grandes poderes... Jajaja\nEste es el segundo archivo que he creado\nEn esta ocación elegí la direección en donde quise guardarlo')

    print(f'Después se escribieron {c} caracteres')
