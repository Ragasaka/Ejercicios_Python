import Ques_by_Kevin

s = input('Ingrese la palabra que quiere desmenuzar: ') 

my_que = Ques_by_Kevin.Que()

print('Se llena la cola.')
 
for x in s :
    my_que.push(x)  

print('Se usa el comando para mostrar la cola')

my_que.show()

print('Ahora se mostrara el procesos de retorno')

for i in range(0,len(s)) :
    input('Presione cualquier tecla : ')
    print(my_que.pop())

h= my_que.pop()