from db_producao.conexao import Conexao
class MaquinasController():

    def __init__(self):
        db = Conexao()
        self.conn = db.get_conexao()
        self.cursor = db.get_cursor()

    def get_conn(self):
        return self.conn

    def get_cursor(self):
        return self. cursor

    def listar(self):
        self.get_cursor().execute("SELECT * FROM maquinas;")
        lin_banco = self.get_cursor().fetchall()
        lista_auxiliar =[]
        for linha in lin_banco:
            dicionario = {
                'id':linha[0],
                'descricao':linha[1],
                'status':linha[2]
            }
            lista_auxiliar.append(dicionario)
        return lista_auxiliar

    def buscar_por_id(self, id):
        self.get_cursor().execute(f"SELECT * FROM maquinas WHERE ordem_id ={id};")
        linha = self.get_cursor().fetchone()
        dicionario = {
            'id': linha[0],
            'descricao': linha[1],
            'status': linha[2]
        }
        return dicionario

    def incluir(self):
        self.get_cursor.execute("INSERT INTO maquinas (descricao, status) VALUES ('Maquina de Solda', 'Ativa');")
        self.get_conn.commit()
        return self.get_cursor().rowcount > 0

    def atualizar(self, id, descricao, status):
        self.cursor.execute("UPDATE maquinas SET descricao = %s, status = %s WHERE maquina_id = %s;", (descricao, status, id))
        self.get_conn().commit()
        return "Maquina atualizado com sucesso."

    def excluir(self, id):
        self.get_cursor().execute(
            "DELETE FROM maquinas WHERE maquina_id = %s;",
            (id,)
        )
        self.get_conn().commit()
        return "Máquina eliminado com sucesso!"