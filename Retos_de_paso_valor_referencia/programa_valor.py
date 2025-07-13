

def  trunca_programa_valor (e, f) :
    g = e[0]
    e[0] = f[0]
    f[0] = g

    return e, f

def main_valor ():
    a = 45
    b = 120.3

    p = 0
    q = 0

    import programa_referencia
    p, q = programa_referencia.trunca_programa_referencia(a,b)

    print('La variables originales son')
    print(f'a = {a}')
    print(f'b = {b}')
    print('La variables retornadas son')
    print(f'p = {p}')
    print(f'q = {q}')
