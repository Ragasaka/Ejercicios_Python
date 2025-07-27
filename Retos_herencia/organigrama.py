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
            print(f'{self.name} todavía no tiene un projecto assignado')

class ProjectManager (employe) :

    def __init__(self, name : str, id :int):
        super().__init__ (name, id)
        self.colaborators = []

    def hire (self, dev):
        self.colaborators.append((dev.name, dev.id))
        dev.assign_project(self.project)
    
    def fire (self, dev):
        if ((dev.name, dev.id) in self.colaborators) :
            self.colaborators.remove((dev.name, dev.id))
            dev.assign_project('')

    def gestiona_proyecto (self) :
        if (self.project != '') :
            print(f'{self.name} está gestionando el proyecto {self.project}')
        else: 
            print(f'{self.name} todavía no tiene un projecto assignado')


class Manager (employe) :
    def __init__(self, name, id):
        super().__init__(name, id) 
        self.projects_list = []
        self.p_managers_list = []
    
    def clientes (self) :
        print(f'{self.name} negocia con los clientes')

    def proveedores (self) :
        print(f'{self.name} negocia con los proveedores')

    def create_project (self, p_manager, project) :
        self.projects_list.append(project)
        self.p_managers_list.append((p_manager.name, p_manager.id))
        p_manager.assign_project(project)


# Crea programadores

paco = developer('Paco', 0)
maria = developer('María', 1)
juan = developer('Juan', 2)

# Crea project managers

mauricio = ProjectManager('Mauricio', 3)
blanca = ProjectManager('Blanca', 4)

mauricio.hire(paco)
mauricio.hire(maria)
blanca.hire(juan)

blanca.gestiona_proyecto()
mauricio.gestiona_proyecto()

#Crea manager

nabor = Manager('Nabor Gonzales', 5)

nabor.create_project(blanca, 'Banda transportadora de empanadas vegetarianas')
nabor.create_project(mauricio, 'Monitor de motores')

print(f'Don {nabor.name} tiene los siguientes proyectos a su mando: \n {nabor.projects_list}')
print(f'Don {nabor.name} tiene los siguientes project managers a su mando: \n {nabor.p_managers_list}')

nabor.clientes()
nabor.proveedores()

print(f'{blanca.name} tiene los siguientes programadores a su mando {blanca.colaborators}')
print(f'{mauricio.name} tiene los siguientes programadores a su mando {mauricio.colaborators}')

mauricio.gestiona_proyecto()
blanca.gestiona_proyecto()