
# Ejemplo de paso por valor

def suma_cualquier_cosa (num1, num2) :
    num1 = num1 + 1
    num2 = num2 - 1
    print(f'num1 es {num1}')
    print(f'num2 es {num2}')

def cambia_string (word) :
    word = word + ' !'
    print(word)

# Con enteros
x = 2
y = 3
suma_cualquier_cosa (x, y) 

print(f'x es {x}')
print(f'y es {y}')

# Con flotantes
x = 2.7
y = 3.6
suma_cualquier_cosa (x, y) 

print(f'x es {x}')
print(f'y es {y}')

# Con complejos 

x = 2 + 3j
y = 3 - 9j
suma_cualquier_cosa (x, y) 

print(f'x es {x}')
print(f'y es {y}')

# Con string

s = 'Hola'
cambia_string(s)

print(f'Realmente era {s}')