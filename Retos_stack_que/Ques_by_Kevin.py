class Que ():
    def __init__ (self) :
       self.a_que = []
    def push (self, object):
        self.a_que.append(object)
    def pop (self) :
        if (len(self.a_que) == 0) :
            print('Cola vacía')
        else :
            return self.a_que.pop(0)
    def show (self) :
        if (len(self.a_que) == 0) :
            print('Cola vacía')
        else :
            for i in range(0, len(self.a_que),1) :
                print(self.a_que[i])