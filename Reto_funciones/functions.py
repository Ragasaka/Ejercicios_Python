import math
def magnitude (vector) :
    a = 0
    for i in vector :
        a += i**2
    return math.sqrt(a)

def uni_vector(magnitude, vector) :
    uni_vector = []
    for x in vector :
        uni_vector.append(x/magnitude)
    return uni_vector

def auto_uni_vector(vector, fun1, fun2): 
    return fun2(fun1(vector), vector)

def factorial (x) :
    if(type(x) == type(1)):
        x = abs(x)
        if(x > 0):
            fact = x*factorial(x-1)
            print(fact)
        else : 
            fact = 1
        return fact
    else : 
        print('Prueba con un número entero')

def combination_counter (a) :
    return lambda n : a ** n

def pure_factorial(x) :
    if x == 0 :
        res = 1
    else : 
        res = x*pure_factorial(x-1)
    return res

def function_positive_verificator(function) : 
    def verify(n):
        print(n)
        if(n < 0) :
            print('Prueba poniendo un número positivo')
        else:
            return function(n)
    return verify

def function_type_verificator(function):
    def typen (n) :
        if(type(n) != type(1)) :
            print('Pon un número entero')
        else: 
            function(n)
    return typen


x, y, z = 0, 3, 4
vector = [x, y, z]
modul = magnitude (vector)

print(f'La magnitud del vector {vector} es {modul}')

vector_unit =  uni_vector(modul, vector)

print(f'El vector unitario de {vector} es {vector_unit}')


vector[0] = 150
vector[1] = vector[1]*math.tanh(0.5) + 330*math.cos(math.pi/6)
vector[2] = vector[2] + 1000

print(f'\nAhora el vector unitario de {vector} es {auto_uni_vector(vector, magnitude, uni_vector)}')

print('\nAcá viene un ejemplo de una función recursiva')
factorial (4)

base = 2
number_bits = 10
combs_base_two = combination_counter (base)

print(f'\n El número de combinaciones de {number_bits} bits es {combs_base_two(number_bits)}')

factorial_v2 = function_positive_verificator(pure_factorial)
fact = factorial_v2(-3)
fact = factorial_v2(4)

print(fact)

factorial_v3 = function_type_verificator(function_type_verificator(pure_factorial))

fact_again = factorial_v3(3)
print(fact_again)