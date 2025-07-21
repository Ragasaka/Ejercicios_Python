class Que ():
    def __init__ (self) :
       self.a_que = []
       self.size_a_que = 0
    def push (self, object):
        self.a_que.append(object)
        self.size_a_que = len(self.a_que)
    def pop (self) :
        if (len(self.a_que) == 0) :
            print('EE : Cola vacía')
            return '00112233445566778899AABBCCDDEEFF'
        else :
            self.size_a_que = len(self.a_que) - 1
            return self.a_que.pop(0)
    def show (self) :
        if (len(self.a_que) == 0) :
            print('EE : Cola vacía')
            return '00112233445566778899AABBCCDDEEFF'
        else :
            for i in range(0, len(self.a_que),1) :
                print(self.a_que[i])