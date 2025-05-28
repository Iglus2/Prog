class Consulta:
    def __init__(self, data, horario, paciente, medico):
        self.data = data
        self.horario = horario
        self.paciente = paciente
        self.medico = medico
        
    def __str__(self):
        return f'''
        Data da Consulta:{self.data}
        Hora da Consulta:{self.horario}
        Nome do Paciente:{self.paciente}
        Médico:{self.medico}    
    '''