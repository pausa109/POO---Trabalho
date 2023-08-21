class MedicamentoQuimioterapico:
    """
    Classe que representa um medicamento quimioterápico.

    Atributos:
        _nome (str): Nome do medicamento.
        _principal_composto (str): Principal composto do medicamento.
        _laboratorio (str): Laboratório que produz o medicamento.
        _descricao (str): Descrição do medicamento.
        _necessita_receita (bool): Indica se o medicamento necessita de receita.
        _preco (float): Preço do medicamento.

    Métodos:
        nome (property): Getter e setter para o nome do medicamento.
        principal_composto (property): Getter e setter para o principal composto do medicamento.
        laboratorio (property): Getter e setter para o laboratório do medicamento.
        descricao (property): Getter e setter para a descrição do medicamento.
        necessita_receita (property): Getter e setter para a informação de necessidade de receita.
        preco (property): Getter e setter para o preço do medicamento.
        __str__(): Retorna uma representação em string do medicamento.
    """
    
    def __init__(self, nome, principal_composto, laboratorio, descricao, necessita_receita, preco):
        self._nome = nome
        self._principal_composto = principal_composto
        self._laboratorio = laboratorio
        self._descricao = descricao
        self._necessita_receita = necessita_receita
        self._preco = preco

    def __str__(self):
        return f"Medicamento Quimioterápico: {self._nome} (Laboratório: {self._laboratorio})"
    
    @property
    def nome(self):
        """Getter para o nome do medicamento."""
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        """Setter para o nome do medicamento."""
        self._nome = novo_nome
    
    @property
    def principal_composto(self):
        """Getter para o principal composto do medicamento."""
        return self._principal_composto
    
    @principal_composto.setter
    def principal_composto(self, novo_composto):
        """Setter para o principal composto do medicamento."""
        self._principal_composto = novo_composto
    
    @property
    def laboratorio(self):
        """Getter para o laboratório do medicamento."""
        return self._laboratorio
    
    @laboratorio.setter
    def laboratorio(self, novo_laboratorio):
        """Setter para o laboratório do medicamento."""
        self._laboratorio = novo_laboratorio
    
    @property
    def descricao(self):
        """Getter para a descrição do medicamento."""
        return self._descricao
    
    @descricao.setter
    def descricao(self, nova_descricao):
        """Setter para a descrição do medicamento."""
        self._descricao = nova_descricao
    
    @property
    def necessita_receita(self):
        """Getter para a informação de necessidade de receita."""
        return self._necessita_receita
    
    @necessita_receita.setter
    def necessita_receita(self, necessita):
        """Setter para a informação de necessidade de receita."""
        self._necessita_receita = necessita

    @property
    def preco(self):
        """Getter para o preço do medicamento."""
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        """Setter para o preço do medicamento."""
        self._preco = novo_preco        


class MedicamentoFitoterapico:
    """
    Classe que representa um medicamento fitoterápico.

    Atributos:
        _nome (str): Nome do medicamento.
        _principal_composto (str): Principal composto do medicamento.
        _laboratorio (str): Laboratório que produz o medicamento.
        _descricao (str): Descrição do medicamento.
        _preco (float): Preço do medicamento.

    Métodos:
        nome (property): Getter e setter para o nome do medicamento.
        principal_composto (property): Getter e setter para o principal composto do medicamento.
        laboratorio (property): Getter e setter para o laboratório do medicamento.
        descricao (property): Getter e setter para a descrição do medicamento.
        preco (property): Getter e setter para o preço do medicamento.
        __str__(): Retorna uma representação em string do medicamento.
    """
    
    def __init__(self, nome, principal_composto, laboratorio, descricao, preco):
        self._nome = nome
        self._principal_composto = principal_composto
        self._laboratorio = laboratorio
        self._descricao = descricao
        self._preco = preco
        

    def __str__(self):
        return f"Medicamento Fitoterápico: {self._nome} (Laboratório: {self._laboratorio})"
    
    @property
    def nome(self):
        """Getter para o nome do medicamento."""
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        """Setter para o nome do medicamento."""
        self._nome = novo_nome
    
    @property
    def principal_composto(self):
        """Getter para o principal composto do medicamento."""
        return self._principal_composto
    
    @principal_composto.setter
    def principal_composto(self, novo_composto):
        """Setter para o principal composto do medicamento."""
        self._principal_composto = novo_composto
    
    @property
    def laboratorio(self):
        """Getter para o laboratório do medicamento."""
        return self._laboratorio
    
    @laboratorio.setter
    def laboratorio(self, novo_laboratorio):
        """Setter para o laboratório do medicamento."""
        self._laboratorio = novo_laboratorio
    
    @property
    def descricao(self):
        """Getter para a descrição do medicamento."""
        return self._descricao
    
    @descricao.setter
    def descricao(self, nova_descricao):
        """Setter para a descrição do medicamento."""
        self._descricao = nova_descricao

    @property
    def preco(self):
        """Getter para o preço do medicamento."""
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        """Setter para o preço do medicamento."""
        self._preco = novo_preco


