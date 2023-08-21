from datetime import datetime
from Clientes import Cliente
from Medicamentos import MedicamentoQuimioterapico, MedicamentoFitoterapico
from Laboratorios import Laboratorio
from Vendas import Venda



def cadastrar_cliente():
    cpf = input("CPF do cliente: ")
    nome = input("Nome do cliente: ")
    data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
    cliente = Cliente(cpf, nome, data_nascimento)
    clientes_cadastrados.append(cliente)
    print("Cliente cadastrado com sucesso!")

def buscar_cliente_por_cpf():
    cpf_busca = input("Digite o CPF do cliente: ")
    cliente_encontrado = next((cliente for cliente in clientes_cadastrados if cliente.cpf == cpf_busca), None)
    if cliente_encontrado:
        print("Cliente encontrado:")
        print(f"Nome: {cliente_encontrado.nome}")
        print(f"CPF: {cliente_encontrado.cpf}")
        print(f"Data de Nascimento: {Cliente.formatar_data(cliente_encontrado.data_nascimento)}")
    else:
        print("Cliente não encontrado.")


def cadastrar_medicamento():
    print("Tipo de medicamento:")
    print("1 - Medicamento Quimioterápico")
    print("2 - Medicamento Fitoterápico")
    tipo_medicamento = input("Escolha o tipo de medicamento: ")

    nome = input("Nome do medicamento: ")
    principal_composto = input("Principal composto: ")
    laboratorio = input("Laboratório: ")
    descricao = input("Descrição: ")

    if tipo_medicamento == "1":
        necessita_receita = input("Necessita de receita? (S/N): ").lower() == "s"
        medicamento = MedicamentoQuimioterapico(nome, principal_composto, laboratorio, descricao, necessita_receita)
        medicamentos_quimioterapicos.append(medicamento)
        print("Medicamento quimioterápico cadastrado com sucesso!")
    elif tipo_medicamento == "2":
        medicamento = MedicamentoFitoterapico(nome, principal_composto, laboratorio, descricao)
        medicamentos_fitoterapicos.append(medicamento)
        print("Medicamento fitoterápico cadastrado com sucesso!")
    else:
        print("Opção inválida para tipo de medicamento.")

def buscar_medicamento():
    print("Opções de busca de medicamento:")
    print("1 - Por nome")
    print("2 - Por fabricante")
    print("3 - Por descrição parcial")
    opcao_busca = input("Escolha uma opção de busca: ")

    termo_busca = input("Digite o termo de busca: ").lower()

    medicamentos_encontrados = []

    if opcao_busca == "1":
        medicamentos_encontrados = [med for med in medicamentos_quimioterapicos + medicamentos_fitoterapicos if termo_busca in med.nome.lower()]
    elif opcao_busca == "2":
        medicamentos_encontrados = [med for med in medicamentos_quimioterapicos + medicamentos_fitoterapicos if termo_busca in med.laboratorio.lower()]
    elif opcao_busca == "3":
        medicamentos_encontrados = [med for med in medicamentos_quimioterapicos + medicamentos_fitoterapicos if termo_busca in med.descricao.lower()]
    else:
        print("Opção inválida para busca.")

    if medicamentos_encontrados:
        print("Medicamentos encontrados:")
        for med in medicamentos_encontrados:
            print(med)
    else:
        print("Nenhum medicamento encontrado.")



def realizar_venda():
    pass

def emitir_relatorios():
    opcao_relatorio = input("Escolha um relatório:\n"
                            "1 - Listagem de clientes em ordem alfabética\n"
                            "2 - Listagem de medicamentos em ordem alfabética\n"
                            "3 - Listagem de medicamentos Quimioterápicos\n"
                            "4 - Listagem de medicamentos Fitoterápicos\n"
                            "Escolha: ")

    if opcao_relatorio == "1":
        clientes_ordenados = sorted(clientes_cadastrados, key=lambda cliente: cliente.nome)
        print("Listagem de clientes em ordem alfabética:")
        for cliente in clientes_ordenados:
            print(cliente)
    elif opcao_relatorio == "2":
        medicamentos_ordenados = sorted(medicamentos_quimioterapicos + medicamentos_fitoterapicos, key=lambda med: med.nome)
        print("Listagem de medicamentos em ordem alfabética:")
        for med in medicamentos_ordenados:
            print(med)
    elif opcao_relatorio == "3":
        medicamentos_quimio = [med for med in medicamentos_quimioterapicos if isinstance(med, MedicamentoQuimioterapico)]
        print("Listagem de medicamentos Quimioterápicos:")
        for med in medicamentos_quimio:
            print(med)
    elif opcao_relatorio == "4":
        medicamentos_fito = [med for med in medicamentos_fitoterapicos if isinstance(med, MedicamentoFitoterapico)]
        print("Listagem de medicamentos Fitoterápicos:")
        for med in medicamentos_fito:
            print(med)
    else:
        print("Opção inválida para relatório.")


# Inicialização de listas e dicionários
clientes_cadastrados = []
medicamentos_quimioterapicos = []
medicamentos_fitoterapicos = []
laboratorios_cadastrados = []
vendas_realizadas = []

# Loop principal do programa
while True:
    print("Menu:")
    print("1 - Cadastrar cliente")
    print("2 - Buscar cliente por CPF")
    print("3 - Cadastrar medicamento")
    print("4 - Buscar medicamento")
    print("5 - Realizar venda")
    print("6 - Emitir relatórios")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        buscar_cliente_por_cpf()
    elif opcao == "3":
        cadastrar_medicamento()
    elif opcao == "4":
        buscar_medicamento()
    elif opcao == "5":
        realizar_venda()
    elif opcao == "6":
        emitir_relatorios()
    elif opcao == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Escolha novamente.")
