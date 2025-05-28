class Pessoa:
    def __init__(self, nome, dt_nasc, email):
        self.nome = nome 
        self.data_nascimento = dt_nasc
        self.email = email
        
    def __str__(self):
        return f'''
        Nome do paciente:{self.nome}
        Data de Nascimento:{self.data_nascimento}
        Email: {self.email}
    '''