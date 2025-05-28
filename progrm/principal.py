from pessoa import Pessoa
from paciente import Paciente
from consulta import Consulta
from medico import Medico




medico = Medico("Johnny", "Johnnyben10legal@outlook.com", "07/08/1990", "Neurocirurgia", "185275")
senha = 1234

class Menu:
    def usuario():
        while True:
            try:
                usuario = int(input("Você é paciente(1) ou médico?(2) "))        
            except ValueError:
                print("Digite apenas número, 1 ou 2")
                continue

            if usuario == 2:
                while True:
                    while True:
                        try:
                            senha_usuario = int(input("Digite a senha: ")) #a senha é 1234 não conta pra ngm
                            break
                        except ValueError:
                            print("A senha é só números")
                            continue
                    if senha_usuario != senha:
                        print("Senha errada!")
                        continue
                    else:
                        break
                print("Senha certa")
                print("1- CADASTRAR PACIENTE")
                print("2- REMOVER PACIENTE")
                print("3- CONSULTAR PACIENTES")
                print("4- CADASTRAR CONSULTA")
                print("5- REMOVER CONSULTA")
                print("6- CONSULTAR CONSULTAS")
                escolha = input("")

                if escolha == '1':
                    nome = input("Nome: ") 
                    email = input("Email: ")
                    dt_nasc = input("Data de nascimento: ")
                    telefone = input("Telefone: ")
                    tps = input("Tipo sanguíneo: ")

                    medico.cadastrarPaciente(nome, email, dt_nasc, telefone, tps)
                elif escolha == '2':
                    nome = input("Digite o nome do paciente que deseja remover: ")
                    medico.removerPaciente(nome)

                elif escolha == '3':
                    medico.consultarPacientes()

                elif escolha == '4':
                    data = input("Data: ") 
                    horario = input("Horario: ")
                    medicoc = input("Medico: ")
                    paciente = input("Paciente: ")

                    medico.cadastrarConsulta(data, horario, medicoc, paciente)
                
                elif escolha == '6':
                    medico.consultarConsultas()

                

            if usuario == 1:
                print("Paciente")


Menu.usuario()