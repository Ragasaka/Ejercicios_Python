import Ques_by_Kevin

command = ''
archive = Ques_by_Kevin.Que()
running = True

while(running) :
    command = input('Ejecutar : ')
    match command :

        case 'E' | 'e' :
            print('Fin de programa')
            running = not(running)
            
        case 'P' | 'p' :
            print(f'{archive.pop()} ha sido impreso')

        case _ :
            archive.push(command)