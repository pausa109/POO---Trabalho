class Laboratorio:
    """
    Classe que representa um laboratório.

    Atributos:
        _nome (str): Nome do laboratório.
        _endereco (str): Endereço do laboratório.
        _telefone (str): Telefone para contato do laboratório.
        _cidade (str): Cidade onde o laboratório está localizado.
        _estado (str): Estado onde o laboratório está localizado.

    Métodos:
        nome (property): Getter e setter para o nome do laboratório.
        endereco (property): Getter e setter para o endereço do laboratório.
        telefone (property): Getter e setter para o telefone do laboratório.
        cidade (property): Getter e setter para a cidade do laboratório.
        estado (property): Getter e setter para o estado do laboratório.
        __str__(): Retorna uma representação em string do laboratório.
    """
    
    def __init__(self, nome, endereco, telefone, cidade, estado):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cidade = cidade
        self._estado = estado

    def __str__(self):
        return f"Laboratório: {self._nome} (Cidade: {self._cidade}, Estado: {self._estado})"
    
    @property
    def nome(self):
        """Getter para o nome do laboratório."""
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        """Setter para o nome do laboratório."""
        self._nome = novo_nome
    
    @property
    def endereco(self):
        """Getter para o endereço do laboratório."""
        return self._endereco
    
    @endereco.setter
    def endereco(self, novo_endereco):
        """Setter para o endereço do laboratório."""
        self._endereco = novo_endereco
    
    @property
    def telefone(self):
        """Getter para o telefone do laboratório."""
        return self._telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        """Setter para o telefone do laboratório."""
        self._telefone = novo_telefone
    
    @property
    def cidade(self):
        """Getter para a cidade do laboratório."""
        return self._cidade
    
    @cidade.setter
    def cidade(self, nova_cidade):
        """Setter para a cidade do laboratório."""
        self._cidade = nova_cidade
    
    @property
    def estado(self):
        """Getter para o estado do laboratório."""
        return self._estado
    
    @estado.setter
    def estado(self, novo_estado):
        """Setter para o estado do laboratório."""
        self._estado = novo_estado
