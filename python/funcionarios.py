class Funcionarios():

    def __init__(self, funcionario_id, nome, setor):
        self._funcionario_id = funcionario_id
        self._nome = nome
        self._setor = setor

    def get_funcionario_id(self):
        return self._funcionario_id

    def set_funcionario_id(self, funcionario_id):
        self._funcionario_id = funcionario_id

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_setor(self):
        return self._nome

    def set_setor(self, setor):
        self._setor = setor




