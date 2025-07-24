class employe :
    def __init__(self, name : str, id : int):
        self.name = name
        self.id = id
        self.project = ''

    def assign_project (self, project : str) :
        if (self.project != '') :
            print(f'{self.name} ya asignado al proyecto {self.project}')
        else :
            self.project = project
    
class developer (employe) :
    
    def code (self):
        if (self.project != '') :
            print(f'{self.name} está escribiendo código para el proyecto {self.project}')
        else: 
            print(F'{self.name} todavía no tiene un projecto assignado')

    def test (self) :

        if (self.project != '') :
            print(f'{self.name} está revisando el código para el proyecto {self.project}')
        else: 
            print(F'{self.name} todavía no tiene un projecto assignado
