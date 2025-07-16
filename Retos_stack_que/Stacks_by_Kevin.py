class Stacks () :
    def __init__(self):
        self.a_stack = []

    def push_stack (self, object) :
        self.a_stack.append(object)

    def pop_stack (self) :
        if(len(self.a_stack) == 0):
            print('Este stack está vacío')
            return '00112233445566778899AABBCCDDEEFF'
        else :
            return self.a_stack.pop()
    
    def show_stack (self) :
        for x in range(0, len(self.a_stack), 1) :
            print(self.a_stack[x])