import Stacks_by_Kevin

running = True
current_page = 'Home'
command = ''
pages_history = Stacks_by_Kevin.Stacks()

while (running) :
    command = input('Ejecutar : ')
    match command :

        case 'E' | 'e' :
            print('Fin de programa')
            running = not(running)
            
        case 'F' | 'f' :
            pages_history.push_stack(current_page)
            current_page = input('Ir a:')
            print(f'Ahora estamos en {current_page}')

        case 'B' | 'b' :
            current_page = pages_history.pop_stack()
            print(f'Ahora estamos en {current_page}')

        case _ :
            print('''Comando inválido prueba ingresando:
                  E o e para salir
                  F o f para ir a otra página
                  B o b para retroceder de página''')
            

