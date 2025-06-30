class Maquinas():

    def __init__(self, maquina_id, descricao, status):
        self._maquina_id = maquina_id
        self._descricao = descricao
        self._status = status

    def get_maquina_id(self):
        return self._maquina_id

    def set_maquina_id(self, maquina_id):
        set._maquina_id = maquina_id

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, descricao):
        set._descricao = descricao

    def get_status(self):
        return self._status

    def set_status(self, status):
        set._status = status


