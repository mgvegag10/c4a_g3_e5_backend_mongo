from flask import jsonify, Blueprint, request
from Controladores.ControladorResultado import ControladorResultado

miControladorResultado = ControladorResultado()

resultado = Blueprint('resultado',__name__)

@resultado.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify(json)
@resultado.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['POST'])
def crearResultado(id_candidato,id_mesa):
    data = request.get_json()
    json=miControladorResultado.create(data,id_candidato,id_mesa)
    return jsonify(json)
@resultado.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)
@resultado.route("/resultados/<string:id>/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['PUT'])
def modificarResultado(id,id_candidato,id_mesa):
    data = request.get_json()
    json=miControladorResultado.update(id,data,id_candidato,id_mesa)
    return jsonify(json)

@resultado.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarResultado(id):
    json=miControladorResultado.delete(id)
    return jsonify(json)