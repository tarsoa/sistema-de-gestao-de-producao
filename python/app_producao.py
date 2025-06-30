from flask import Flask, jsonify, request

from db_producao.funcionarios_controller import FuncionariosController
from db_producao.maquinas_controller import MaquinasController
from db_producao.ordens_producao_controller import OrdensProducaoController

app_producao = Flask(__name__)

funcionario = FuncionariosController()
maquina = MaquinasController()
ordens_producao = OrdensProducaoController()

# ============================= FUNCIONÁRIOS =============================

@app_producao.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    dados = funcionario.listar()
    return jsonify(dados)

@app_producao.route('/funcionarios/<int:id>', methods=['GET'])
def buscar_funcionario_por_id(id):
    dado = funcionario.buscar_por_id(id)
    if dado:
        return jsonify(dado)
    return jsonify({"erro": "Funcionário não encontrado"}), 404

@app_producao.route('/funcionarios', methods=['POST'])
def incluir_funcionario():
    dado = request.get_json()
    funcionario.incluir(dado['nome'], dado['setor'])
    return jsonify({"mensagem": "Funcionário incluído com sucesso"}), 201

@app_producao.route('/funcionarios', methods=['PUT'])
def atualizar_funcionario():
    dado = request.get_json()
    funcionario.atualizar(dado['id'], dado['nome'], dado['setor'])
    return jsonify({"mensagem": "Funcionário atualizado com sucesso"})

@app_producao.route('/funcionarios/<int:id>', methods=['DELETE'])
def remover_funcionario(id):
    func = funcionario.buscar_por_id(id)
    if not func:
        return jsonify({"erro": "Funcionário não encontrado"}), 404
    funcionario.excluir(id)
    return jsonify({"mensagem": "Funcionário removido com sucesso"})

# ============================= MÁQUINAS =============================

@app_producao.route('/maquinas', methods=['GET'])
def listar_maquinas():
    dados = maquina.listar()
    return jsonify(dados)

@app_producao.route('/maquinas/<int:id>', methods=['GET'])
def buscar_maquina_por_id(id):
    dado = maquina.buscar_por_id(id)
    if dado:
        return jsonify(dado)
    return jsonify({"erro": "Máquina não encontrada"}), 404

@app_producao.route('/maquinas', methods=['POST'])
def incluir_maquina():
    dado = request.get_json()
    maquina.incluir(dado['descricao'], dado['status'])
    return jsonify({"mensagem": "Máquina incluída com sucesso"}), 201

@app_producao.route('/maquinas', methods=['PUT'])
def atualizar_maquina():
    dado = request.get_json()
    maquina.atualizar(dado['id'], dado['descricao'], dado['status'])
    return jsonify({"mensagem": "Máquina atualizada com sucesso"})

@app_producao.route('/maquinas/<int:id>', methods=['DELETE'])
def remover_maquina(id):
    maq = maquina.buscar_por_id(id)
    if not maq:
        return jsonify({"erro": "Máquina não encontrada"}), 404
    maquina.excluir(id)
    return jsonify({"mensagem": "Máquina removida com sucesso"})

# ============================= ORDENS DE PRODUÇÃO =============================

@app_producao.route('/ordens_producao', methods=['GET'])
def listar_ordens_producao():
    dados = ordens_producao.listar()
    return jsonify(dados)

@app_producao.route('/ordens_producao/<int:id>', methods=['GET'])
def buscar_ordem_por_id(id):
    dado = ordens_producao.buscar_por_id(id)
    if dado:
        return jsonify(dado)
    return jsonify({"erro": "Ordem de produção não encontrada"}), 404

@app_producao.route('/ordens_producao', methods=['POST'])
def incluir_ordem_producao():
    dado = request.get_json()
    ordens_producao.incluir(dado['produto'], dado['quantidade'], dado['status'])
    return jsonify({"mensagem": "Ordem de produção incluída com sucesso"}), 201

@app_producao.route('/ordens_producao', methods=['PUT'])
def atualizar_ordem_producao():
    dado = request.get_json()
    ordens_producao.atualizar(dado['id'], dado['produto'], dado['quantidade'], dado['status'])
    return jsonify({"mensagem": "Ordem de produção atualizada com sucesso"})

@app_producao.route('/ordens_producao/<int:id>', methods=['DELETE'])
def remover_ordem_producao(id):
    ordem = ordens_producao.buscar_por_id(id)
    if not ordem:
        return jsonify({"erro": "Ordem de produção não encontrada"}), 404
    ordens_producao.excluir(id)
    return jsonify({"mensagem": "Ordem de produção removida com sucesso"})

# ============================= DEBUG =============================
# print(funcionario.listar())
# print(maquina.listar())
print(ordens_producao.listar())

# ============================= EXECUTAR APP =============================
if __name__ == '__main__':
    app_producao.run(debug=True)
