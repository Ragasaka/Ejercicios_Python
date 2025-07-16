def numero_fibonacci (n : int) -> int :
    if (n >= 3) :
        return numero_fibonacci(n - 1) + numero_fibonacci(n - 2)
    else : 
        return 1

r = int(input('Cual número de Fibonacci quiere hallar? '))

fibonacci = numero_fibonacci(r)

print(f'El numero de fibonacci elegido es {fibonacci}')