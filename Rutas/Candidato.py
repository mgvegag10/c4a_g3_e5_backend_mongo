from flask import jsonify, Blueprint, request
from Controladores.ControladorCandidato import ControladorCandidato

miControladorCandidato = ControladorCandidato()

candidato = Blueprint('candidato',__name__)

@candidato.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
@candidato.route("/candidatos",methods=['GET'])
def getPartidos():
    json=miControladorCandidato.index()
    return jsonify(json)
@candidato.route("/candidatos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@candidato.route("/candidatos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@candidato.route("/candidatos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)

@candidato.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)

@candidato.route("/candidatos/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoACandidato(id,id_partido):
    json=miControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)