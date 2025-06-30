class Ordens_producao():

    def __init__(self, ordem_id, funcionario_id, maquina_id, produto, quantidade, status):
        self._ordem_id = ordem_id
        self._funcionario_id = funcionario_id
        self._maquina_id = maquina_id
        self._produto = produto
        self._quantidade = quantidade
        self._status = status

    def get_ordem_id(self):
        return self._ordem_id

    def get_funcionario_id(self):
        return self._funcionario_id

    def set_funcionario_id(self, funcionario_id):
        self._funcionario_id = funcionario_id

    def get_maquina_id(self, maquina_id):
        return self._maquina_id

    def set_maquina_id(self, maquina_id):
        self._maquina_id = maquina_id

    def get_produto(self, produto):
        return self._produto

    def set_produto(self, produto):
        self._produto = produto

    def get_quantidade(self, quantidade):
        return self._quantidade

    def set_quantidade(self, quantidade):
        self._quantidade = quantidade