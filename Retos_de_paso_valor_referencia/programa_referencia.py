def  trunca_programa_referencia (h, i) :
    k = h
    h = i
    i = k

    return h, i

def main_referencia ():
    c = [33]
    d = [1 + 2j]

    import programa_valor

    r, s = programa_valor.trunca_programa_valor(c,d)
    print('La variables originales son')
    print(f'c = {c}')
    print(f'd = {d}')
    print('La variables retornadas son')
    print(f'r = {r}')
    print(f's = {s}')

