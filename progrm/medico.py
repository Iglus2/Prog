from pessoa import Pessoa
from paciente import Paciente
from consulta import Consulta



class Medico(Pessoa):
    def __init__(self, nome, email, dt_nasc, espec, crm):
        super().__init__(nome, email, dt_nasc)
        self.espec = espec
        self.crm = crm

        self.pacientes=[]
        self.consultas=[]

    def __str__(self):
        return f'''
        {super().__str__()},
        especialidade: {self.espec}, 
        Crm: {self.crm}
        '''

    def cadastrarPaciente(self, nome, email, dt_nasc, telefone, tps): #tps é tipo sanguineo
        paciente = Paciente(nome, email, dt_nasc, telefone, tps)
        self.pacientes.append(paciente)

    def removerPaciente(self, nome):
        for paciente in self.pacientes:
            if paciente.nome == nome:
                self.pacientes.remove(paciente)
                print(f"Paciente {nome} removido com sucesso.")
                return
        print(f"Paciente {nome} não encontrado.")
        
    def consultarPacientes(self):
        for paciente in self.pacientes:
            print(paciente)
    def removerPaciente(self, data):
        for consulta in self.consultas:
            if consulta.nome == data:
                self.pacientes.remove(data)
                print(f"Consulta da data {data} foi removida com sucesso.")
                return
        print(f"Consulta da data {data} não foi encontrada.")

    def cadastrarConsulta(self, data, horario, medico, paciente):
        consulta = Consulta(data, horario, medico, paciente)
        self.consultas.append(consulta)
        
    def consultarConsultas(self):
        for consulta in self.consultas:
            print(consulta)
