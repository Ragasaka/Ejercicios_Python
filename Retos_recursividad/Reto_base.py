def impresion_recursiva (z : int) :
    if( z >= 0) :
        print(z)
        impresion_recursiva(z-1)

impresion_recursiva(100)