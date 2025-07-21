import Retos_stack_que.Stacks_by_Kevin as Stacks_by_Kevin

n = 5
my_stack = Stacks_by_Kevin.Stacks()

for i in range(0, n) :
    my_stack.push_stack(input())

print('El stack resultante es este')
my_stack.show_stack()
print('Ahora mostremos elemento por elemento')

for i in range(0, n) :
    input('Presione cualquier tecla')
    print(my_stack.pop_stack())
