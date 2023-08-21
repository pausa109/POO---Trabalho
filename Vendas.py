from Medicamentos import MedicamentoQuimioterapico, MedicamentoFitoterapico

class Venda:
    """
    Classe que representa uma venda.

    Atributos:
        _data_hora (str): Data e hora da venda no formato 'YYYY-MM-DD HH:MM:SS'.
        _produtos (list): Lista de produtos vendidos na venda.
        _cliente (Cliente): Cliente associado à venda.
        _valor_total (float): Valor total da venda.

    Métodos:
        data_hora (property): Getter para a data e hora da venda.
        produtos (property): Getter para a lista de produtos vendidos.
        cliente (property): Getter e setter para o cliente associado à venda.
        valor_total (property): Getter para o valor total da venda.
        adicionar_produto(produto): Adiciona um produto à venda.
        calcular_desconto(): Calcula e aplica o desconto na venda.
        verificar_receita(): Verifica a necessidade de receita para medicamentos controlados.
        __str__(): Retorna uma representação em string da venda.
    """
    
    def __init__(self, data_hora, cliente):
        self._data_hora = data_hora
        self._produtos = []
        self._cliente = cliente
        self._valor_total = 0.0

    def __str__(self):
        return f"Venda em {self._data_hora} para o cliente {self._cliente.nome}"

    @property
    def data_hora(self):
        """Getter para a data e hora da venda."""
        return self._data_hora
    
    @property
    def produtos(self):
        """Getter para a lista de produtos vendidos."""
        return self._produtos
    
    @property
    def cliente(self):
        """Getter e setter para o cliente associado à venda."""
        return self._cliente
    
    @cliente.setter
    def cliente(self, novo_cliente):
        """Setter para o cliente associado à venda."""
        self._cliente = novo_cliente
    
    @property
    def valor_total(self):
        """Getter para o valor total da venda."""
        return self._valor_total

    def adicionar_produto(self, produto):
        """Adiciona um produto à venda."""
        self._produtos.append(produto)
        self._valor_total += produto.preco

    def calcular_desconto(self):
        """Calcula e aplica o desconto na venda."""
        desconto_idoso = 0.20 if self._cliente.is_idoso() else 0.0
        desconto_valor = 0.10 if self._valor_total > 150 else 0.0

        if desconto_idoso > desconto_valor:
            self._valor_total -= self._valor_total * desconto_idoso
        elif desconto_valor > 0:
            self._valor_total -= self._valor_total * desconto_valor

    def verificar_receita(self):
        """Verifica a necessidade de receita para medicamentos controlados."""
        for produto in self._produtos:
            if isinstance(produto, MedicamentoQuimioterapico) and produto.necessita_receita:
                return f"Alerta: Verifique a receita para o medicamento {produto.nome}"
        return None

