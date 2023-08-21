from datetime import datetime
from Clientes import Cliente
from Medicamentos import MedicamentoQuimioterapico, MedicamentoFitoterapico
from Laboratorios import Laboratorio
from Vendas import Venda



def cadastrar_cliente():
    """
    Cadastra um novo cliente na farmácia.

    Solicita informações ao usuário (CPF, nome e data de nascimento) e cria um novo objeto Cliente.
    O cliente cadastrado é adicionado à lista clientes_cadastrados.

    Returns:
        None
    """
    cpf = input("CPF do cliente: ")
    nome = input("Nome do cliente: ")
    data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
    cliente = Cliente(cpf, nome, data_nascimento)
    clientes_cadastrados.append(cliente)
    print("Cliente cadastrado com sucesso!")

def buscar_cliente_por_cpf():
    """
    Busca um cliente pelo CPF.

    Solicita o CPF ao usuário e busca na lista clientes_cadastrados pelo cliente correspondente.
    Caso encontrado, exibe as informações do cliente.

    Returns:
        None
    """
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
    """
    Cadastra um novo medicamento na farmácia.

    Solicita informações ao usuário (tipo de medicamento, nome, composto, laboratório, descrição e preço)
    e cria um novo objeto MedicamentoQuimioterapico ou MedicamentoFitoterapico.
    O medicamento cadastrado é adicionado à lista medicamentos_quimioterapicos ou medicamentos_fitoterapicos.

    Returns:
        None
    """
    print("Tipo de medicamento:")
    print("1 - Medicamento Quimioterápico")
    print("2 - Medicamento Fitoterápico")
    tipo_medicamento = input("Escolha o tipo de medicamento: ")

    nome = input("Nome do medicamento: ")
    principal_composto = input("Principal composto: ")
    
    # Lista os laboratórios cadastrados
    print("Laboratórios cadastrados:")
    for i, lab in enumerate(laboratorios_cadastrados, start=1):
        print(f"{i} - {lab.nome}")
    
    # Solicitação do laboratório ao usuário
    lab_choice = int(input("Escolha o número do laboratório: "))
    if lab_choice < 1 or lab_choice > len(laboratorios_cadastrados):
        print("Escolha inválida para laboratório.")
        return
    
    laboratorio = laboratorios_cadastrados[lab_choice - 1]
    
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))  # Solicitação do preço ao usuário

    if tipo_medicamento == "1":
        necessita_receita = input("Necessita de receita? (S/N): ").lower() == "s"
        medicamento = MedicamentoQuimioterapico(nome, principal_composto, laboratorio, descricao, necessita_receita, preco)  # Adiciona o preço ao criar o medicamento
        medicamentos_quimioterapicos.append(medicamento)
        print("Medicamento quimioterápico cadastrado com sucesso!")
    elif tipo_medicamento == "2":
        medicamento = MedicamentoFitoterapico(nome, principal_composto, laboratorio, descricao, preco)  # Adiciona o preço ao criar o medicamento
        medicamentos_fitoterapicos.append(medicamento)
        print("Medicamento fitoterápico cadastrado com sucesso!")
    else:
        print("Opção inválida para tipo de medicamento.")



def buscar_medicamento():
    """
    Busca medicamentos por nome, fabricante ou descrição parcial.

    Solicita ao usuário a opção de busca e um termo de busca.
    Busca na lista de medicamentos por correspondências e exibe os resultados.

    Returns:
        None
    """
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

def cadastrar_laboratorio():
    """
    Cadastra um novo laboratório na farmácia.

    Solicita informações ao usuário (nome, endereço, telefone, cidade, estado) e cria um novo objeto Laboratorio.
    O laboratório cadastrado é adicionado à lista laboratorios_cadastrados.

    Returns:
        None
    """
    nome = input("Nome do laboratório: ")
    endereco = input("Endereço do laboratório: ")
    telefone = input("Telefone do laboratório: ")
    cidade = input("Cidade do laboratório: ")
    estado = input("Estado do laboratório: ")
    laboratorio = Laboratorio(nome, endereco, telefone, cidade, estado)
    laboratorios_cadastrados.append(laboratorio)
    print("Laboratório cadastrado com sucesso!")



def realizar_venda():
    """
    Realiza uma venda na farmácia.

    Solicita o CPF do cliente, busca o cliente correspondente e inicia um objeto Venda.
    Permite adicionar produtos à venda, calcular descontos e verificar receitas.
    Ao final, confirma a venda ou cancela.

    Returns:
        None
    """
    cpf_cliente = input("Digite o CPF do cliente: ")
    cliente_encontrado = next((cliente for cliente in clientes_cadastrados if cliente.cpf == cpf_cliente), None)

    if cliente_encontrado:
        print("Cliente encontrado:")
        print(f"Nome: {cliente_encontrado.nome}")
        print(f"CPF: {cliente_encontrado.cpf}")

        venda = Venda(datetime.now(), cliente_encontrado)

        while True:
            produto_nome = input("Digite o nome do produto a ser vendido (ou 'fim' para encerrar a venda): ")
            if produto_nome == "fim":
                break

            medicamento_encontrado = next((med for med in medicamentos_quimioterapicos + medicamentos_fitoterapicos if med.nome.lower() == produto_nome.lower()), None)
            if medicamento_encontrado:
                venda.adicionar_produto(medicamento_encontrado)
                print(f"Produto {medicamento_encontrado.nome} adicionado à venda.")
            else:
                print("Produto não encontrado.")

        venda.calcular_desconto()

        alerta_receita = venda.verificar_receita()
        if alerta_receita:
            print(alerta_receita)

        print(f"Valor total da venda: R${venda.valor_total:.2f}")

        confirmacao = input("Deseja confirmar a venda? (S/N): ").lower()
        if confirmacao == "s":
            vendas_realizadas.append(venda)
            print("Venda realizada e confirmada!")
        else:
            print("Venda cancelada.")

    else:
        print("Cliente não encontrado.")


def emitir_relatorios():
    """
    Emite relatórios de clientes e medicamentos.

    Exibe opções de relatórios, permitindo listar clientes, medicamentos ou tipos específicos de medicamentos.

    Returns:
        None
    """
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

def gerar_relatorio_estatisticas(vendas):
    """
    Gera um relatório de estatísticas.

    Calcula e exibe estatísticas como o remédio mais vendido, quantidade de pessoas atendidas,
    quantidade de remédios Quimioterápicos e Fitoterápicos vendidos, valores totais e valor total das vendas.

    Args:
        vendas (list): Lista de objetos Venda.

    Returns:
        None
    """
    print("Relatório de Estatísticas:")
    
    # Remédio mais vendido
    produtos_vendidos = [produto for venda in vendas for produto in venda.produtos]
    remedio_mais_vendido = max(produtos_vendidos, key=lambda produto: produtos_vendidos.count(produto))
    quantidade_mais_vendido = produtos_vendidos.count(remedio_mais_vendido)
    valor_total_mais_vendido = quantidade_mais_vendido * remedio_mais_vendido.preco
    print(f"Remédio mais vendido: {remedio_mais_vendido.nome}")
    print(f"Quantidade vendida: {quantidade_mais_vendido}")
    print(f"Valor total: R${valor_total_mais_vendido:.2f}")
    
    # Quantidade de pessoas atendidas
    quantidade_pessoas_atendidas = len(set(venda.cliente for venda in vendas))
    print(f"Quantidade de pessoas atendidas: {quantidade_pessoas_atendidas}")
    
    # Número de remédios Quimioterápicos vendidos
    quantidade_quimioterapicos = sum(1 for venda in vendas for produto in venda.produtos if isinstance(produto, MedicamentoQuimioterapico))
    valor_total_quimioterapicos = sum(produto.preco for venda in vendas for produto in venda.produtos if isinstance(produto, MedicamentoQuimioterapico))
    print(f"Número de remédios Quimioterápicos vendidos: {quantidade_quimioterapicos}")
    print(f"Valor total dos Quimioterápicos: R${valor_total_quimioterapicos:.2f}")
    
    # Número de remédios Fitoterápicos vendidos
    quantidade_fitoterapicos = sum(1 for venda in vendas for produto in venda.produtos if isinstance(produto, MedicamentoFitoterapico))
    valor_total_fitoterapicos = sum(produto.preco for venda in vendas for produto in venda.produtos if isinstance(produto, MedicamentoFitoterapico))
    print(f"Número de remédios Fitoterápicos vendidos: {quantidade_fitoterapicos}")
    print(f"Valor total dos Fitoterápicos: R${valor_total_fitoterapicos:.2f}")
    
    # Valor total das vendas
    valor_total_vendas = sum(venda.valor_total for venda in vendas)
    print(f"Valor total das vendas: R${valor_total_vendas:.2f}")
   


# Inicialização de listas e dicionários
clientes_cadastrados = [
    Cliente("123.456.789-01", "João da Silva", "1990-05-15"),
    Cliente("987.654.321-01", "Maria Souza", "1985-10-25"),
    Cliente("456.789.123-01", "Pedro Oliveira", "2000-02-10")
]

medicamentos_quimioterapicos = [
    MedicamentoQuimioterapico("QuimioA", "CompostoA", "LabA", "Medicamento para tratamento de quimioterapia", True, 100.0),
    MedicamentoQuimioterapico("QuimioB", "CompostoB", "LabB", "Medicamento para tratamento de quimioterapia", True, 200.0)
]

medicamentos_fitoterapicos = [
    MedicamentoFitoterapico("FitA", "ErvaA", "LabA", "Medicamento fitoterápico para relaxamento", 42.00),
    MedicamentoFitoterapico("FitB", "ErvaB", "LabB", "Medicamento fitoterápico para alívio de stress", 57.50)
]

laboratorios_cadastrados = [
    Laboratorio("LabA", "Endereço A", "Telefone A", "Cidade A", "Estado A"),
    Laboratorio("LabB", "Endereço B", "Telefone B", "Cidade B", "Estado B"),
]
vendas_realizadas = []

# Loop principal do programa
while True:
    print("Menu:")
    print("1 - Cadastrar cliente")
    print("2 - Buscar cliente por CPF")
    print("3 - Cadastrar medicamento")
    print("4 - Buscar medicamento")
    print("5 - Cadastrar laboratório")
    print("6 - Realizar venda")
    print("7 - Emitir relatórios")
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
        cadastrar_laboratorio() 
    elif opcao == "6":
        realizar_venda()
    elif opcao == "7":
        emitir_relatorios()
    elif opcao == "0":
        print("Saindo do programa. Emitindo relatório de estatísticas:")
        gerar_relatorio_estatisticas(vendas_realizadas)
        break
    else:
        print("Opção inválida. Escolha novamente.")
