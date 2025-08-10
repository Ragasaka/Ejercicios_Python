
def menu ()-> None:
    print('1. Agregar')
    print('2. Actualizar')
    print('3. Consultar')
    print('4. Eliminar')
    print('5. Salir')

class lista_compras ():
    def __init__(self):
        with open('Lista_movimientos.txt', 'w') as f:
            f.write('Resumén de movimientos')
    def annade_registro

# Programa principal

running = True

while(running):
    menu()
    opt = input('Eliga una opción (número): ')
    match opt:
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
            running = False
        case _:
            print('Pon un valor válido')

