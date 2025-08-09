class KevinError (Exception) :
    pass


def div (a : int, b : int) :
    return a/b

def dumb_func(b : bool) :
    try :
        if(b) :
            return True
        else :
            raise ValueError
    except ValueError :
        raise
        return False
    finally :
        return 'Se acaba de ejecutar dumb_func'

# Generar excepciones por generar excepciones
'''
excepciones = [TypeError('tipo equivocado'), ValueError('valor equivocado'), NameError('tal variable no existe')]

n = 3

try :
    raise excepciones[n]
except Exception as e :
    print('Oops. algo a pasado')
    e.add_note(f'Esta es la excepción {n}')
    raise
'''

# Uso de la palabra else
'''
try :
    c = div(15, 5)
except Exception as e :
    print('Álgo ha salido mal, a la proxima ten más cuidado al llamar la función')
else :
    print(f'El resultado es {c}')

try :
    c = div(15, 0)
except Exception as e :
    print('Álgo ha salido mal, a la proxima ten más cuidado al llamar la función')
else :
    print(f'El resultado es {c}')
'''

# Uso de la palabra finally
'''
try :
    c = div(15, 5)
except Exception as e :
    print('Álgo ha salido mal, a la proxima ten más cuidado al llamar la función')
else :
    print(f'El resultado es {c}')
finally :
    print('Fin de este bloque de código con el comando finally')

print(dumb_func(True))
print(dumb_func(False))
'''

#Una excepción definida por el usuario
try :
    raise KevinError('Kevin no esta permitido en este programa')
except:
    print('Oops... A ocurrido un error')
    raise