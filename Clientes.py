from datetime import datetime
class Cliente:
    """
    Classe que representa um cliente da farmácia.

    Atributos:
        _cpf (str): CPF do cliente (protegido).
        _nome (str): Nome do cliente (protegido).
        _data_nascimento (str): Data de nascimento do cliente no formato 'YYYY-MM-DD' (protegido).

    Métodos:
        cpf (property): Getter para o CPF do cliente.
        nome (property): Getter e setter para o nome do cliente.
        data_nascimento (property): Getter e setter para a data de nascimento do cliente.
        formatar_data(data: str) -> str: Método estático para formatar a data no padrão brasileiro.
    """
    
    def __init__(self, cpf, nome, data_nascimento):
        """
        Inicializa os atributos do cliente.

        Args:
            cpf (str): CPF do cliente.
            nome (str): Nome do cliente.
            data_nascimento (str): Data de nascimento do cliente no formato 'YYYY-MM-DD'.
        """
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def __str__(self):
        return f"Cliente: {self.nome} (CPF: {self._cpf})"
    
    @property
    def cpf(self):
        """Getter para o CPF do cliente."""
        return self._cpf
    
    @property
    def nome(self):
        """Getter para o nome do cliente."""
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        """Setter para o nome do cliente."""
        self._nome = novo_nome
    
    @property
    def data_nascimento(self):
        """Getter para a data de nascimento do cliente."""
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        """Setter para a data de nascimento do cliente, formatada como 'YYYY-MM-DD'."""
        self._data_nascimento = nova_data
    
    @staticmethod
    def formatar_data(data):
        """Método estático para formatar a data no padrão brasileiro 'DD/MM/YYYY'."""
        partes = data.split('-')
        return f"{partes[2]}/{partes[1]}/{partes[0]}"
    
    def checar_idoso(self):
        """Verifica se o cliente é idoso (tem mais de 65 anos)."""
        data_nascimento = datetime.strptime(self._data_nascimento, '%Y-%m-%d')
        hoje = datetime.now()
        idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
        return idade > 65

