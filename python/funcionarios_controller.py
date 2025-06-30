from db_producao.conexao import Conexao
class FuncionariosController():

    def __init__(self):
        db = Conexao()
        self.conn = db.get_conexao()
        self.cursor = db.get_cursor()

    def get_conn(self):
        return self.conn

    def get_cursor(self):
        return self. cursor

    def listar(self):
        self.get_cursor().execute("SELECT * FROM funcionarios;")
        lin_banco = self.get_cursor().fetchall()
        lista_auxiliar =[]
        for linha in lin_banco:
            dicionario = {
                'id':linha[0],
                'nome':linha[1],
                'setor':linha[2]
            }
            lista_auxiliar.append(dicionario)
        return lista_auxiliar

    def buscar_por_id(self, id):
        self.get_cursor().execute(f"SELECT * FROM funcionarios WHERE funcionario_id ={id};")
        linha = self.get_cursor().fetchone()
        dicionario = {
            'id': linha[0],
            'nome': linha[1],
            'setor': linha[2]
        }
        return dicionario

    def incluir(self, nome, setor):
        self.cursor.execute("INSERT INTO funcionarios (nome, setor) VALUES(%s, %s);",(nome,setor))
        self.conn.commit()
        return "Cadastrado com sucesso"

    def atualizar(self, id, nome, setor):
        self.cursor.execute("UPDATE funcionarios SET nome = %s, setor = %s WHERE funcionario_id = %s;", (nome, setor, id))
        self.get_conn().commit()
        return "Funcionario atualizado com sucesso."

    def excluir(self, id):
        self.get_cursor().execute(
            "DELETE FROM funcionarios WHERE funcionario_id = %s;",
            (id,)
        )
        self.get_conn().commit()
        return "Funcionário eliminado com sucesso!"

