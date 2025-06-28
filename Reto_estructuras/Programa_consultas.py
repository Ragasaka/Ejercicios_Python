import Menu_inicio

execution = True
users = {0:{'Nombre':'Camilo', 'Tel':100}, 1:{'Nombre':'Andres', 'Tel':200}, 2:{'Nombre':'Ana', 'Tel':300}}
new_index = len(users)

#Función para cinsultar un usuario por su ID

def query_list (users) : 
    print('Ingrese el número identificador del usuario que quiere consultar')
    try :
        id = int(input())
    except :
        print('Prueba poniendo un número entero')
    else: 
        print(f'El identificador ingresado fue {id}')
        if id in users :
            print(users[id])
        else :
            print('El número ingresado no está en la lista')

# Funció para añadir un nuevo usuario a la lista

def add_user(users, new_index):
    name = input('Ingrese el nombre del nuevo usuario: ')
    n_ok = True
    while(n_ok) :
        try :
            tel = int(input('Ingrese el numero de telefono: '))
        except :
            print('Error: no pusiste un número. Intenta de nuevo')
        else :
            if(tel < 1000) :
                print('Número de telefono válido')
                n_ok = False
            else :
                print('Número no valido. Prueba poniendo uno estrictamente menor a 1000')
    users[new_index] = {'Nombre':name, 'Tel': tel}
    new_index += 1
    print(users)
    return users, new_index

# Función que elimina usuarios

def delete_user(users) :
    print('Ingrese el número identificador del usuario que quiere eliminar')
    try :
        id = int(input())
    except :
        print('Prueba poniendo un número entero')
    else: 
        print(f'El identificador ingresado fue {id}')
        if id in users :
            print(f'El usuario eliminado será : {users[id]}')
            del users[id]
            print(users)
        else :
            print('El número ingresado no está en la lista')
    return users

# Función para actualizar un usuario

def update_user (users) : 
    print('Ingrese el número identificador del usuario que quiere consultar')
    try :
        id = int(input())
    except :
        print('Prueba poniendo un número entero')
    else: 
        print(f'El identificador ingresado fue {id}')
        if id in users :
            #Codigo a reemplazar
            name = input('Ingrese el nuevo nombre del usuario: ')
            n_ok = True
            while(n_ok) :
                try :
                    tel = int(input('Ingrese el numero de telefono: '))
                except :
                    print('Error: no pusiste un número. Intenta de nuevo')
                else :
                    if(tel < 1000) :
                        print('Número de telefono válido')
                        n_ok = False
                    else :
                        print('Número no valido. Prueba poniendo uno estrictamente menor a 1000')
            users[id] = {'Nombre':name, 'Tel': tel}
        else :
            print('El número ingresado no está en la lista')
    return users


while execution :
    Menu_inicio.menu()
    option = input()
    print(f'La entrada es: {option}')
    if (option == '5') :
        execution = False
    if (option == '4') :
        query_list(users)
    if (option == '3') :
        users = update_user(users)
        print(users)
    if (option == '2') :
        users = delete_user(users)
    if (option == '1') :
        payload = add_user(users, new_index)
        users = payload[0]
        new_index = payload[1]
print('Fin de programa')