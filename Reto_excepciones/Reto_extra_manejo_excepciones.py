class TooSmallError (Exception) :
    pass

class TooBigError (Exception) :
    pass

def exc_func (a_list : list) -> None :
    l = len(a_list)
    try:
        if (l == 0) :
            raise TooSmallError('Longitud no válida')
        elif (l > 10) :
            raise TooBigError('Longitud no válida')
        else :
            for x in a_list :
                if(type(x) != type('s')) :
                    print(x)
                else :
                    raise TypeError('Objeto no válido')
                    break

    except TooSmallError as e:
        e.add_note('Esta lista está vacía, prueba poniendo una con al menos un elemento')
        print(f'{type(e).__name__}:{e}')
        print(f'{e.__notes__}')
    
    except TooBigError as e:
        e.add_note('Esta lista demasiado grande, prueba poniendo una con a lo sumo 10 elementos')
        print(f'{type(e).__name__}:{e}')

    except TypeError as e:
        print(f'{type(e).__name__}:{e}')
        e.add_note('Pusiste un elemento no válido, a la proxima pon un número')
        print(f'{e.__notes__}')
        
    else :
        print('Todo ha ido bien.')

# Programa principal.

the_list = [3, 21, 5+7j, 65, 3.14159]

exc_func(the_list)

'''
for i in range(1,15,1) :
    the_list.append(i)

exc_func(the_list)
'''

'''
another_list = []

exc_func(another_list)
'''

the_list.append('Hola')

exc_func(the_list)