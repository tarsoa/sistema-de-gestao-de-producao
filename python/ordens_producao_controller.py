from db_producao.conexao import Conexao
class OrdensProducaoController():

    def __init__(self):
        db = Conexao()
        self.conn = db.get_conexao()
        self.cursor = db.get_cursor()

    def get_conn(self):
        return self.conn

    def get_cursor(self):
        return self. cursor

    def listar(self):
        self.get_cursor().execute("SELECT * FROM ordens_producao;")
        lin_banco = self.get_cursor().fetchall()
        lista_auxiliar =[]
        for linha in lin_banco:
            dicionario = {
                'id':linha[0],
                'produto':linha[3],
                'quantidade':linha[4],
                'status':linha[5]
            }
            lista_auxiliar.append(dicionario)
        return lista_auxiliar

    def buscar_por_id(self, id):
        self.get_cursor().execute(f"SELECT * FROM ordens_producao WHERE ordem_id ={id};")
        linha = self.get_cursor().fetchone()
        dicionario = {
            'id': linha[0],
            'produto': linha[3],
            'quantidade': linha[4],
            'status': linha[5]
        }
        return dicionario

    def incluir(self):
        self.get_cursor.execute("INSERT INTO ordens_producao (produto, quantidade, status) VALUES ('Produto U', '300', 'Em andamento');")
        self.get_conn.commit()
        return self.get_cursor().rowcount > 0

    def atualizar(self, id, produto, quantidade, status):
        self.cursor.execute("UPDATE ordens_producao SET produto = %s, quantidade = %s, status = %s WHERE maquina_id = %s;", (produto, quantidade, status, id))
        self.get_conn().commit()
        return "Ordem atualizado com sucesso."

    def excluir(self, id):
        self.get_cursor().execute(
            "DELETE FROM ordens_producao WHERE ordem_id = %s;",
            (id,)
        )
        self.get_conn().commit()
        return "Ordem de Produção eliminada com sucesso!"



