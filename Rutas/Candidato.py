from flask import jsonify, Blueprint, request
from Controladores.ControladorCandidato import ControladorCandidato

miControladorCandidato = ControladorCandidato()

candidato = Blueprint('candidato',__name__)

@candidato.route("/candidatos",methods=['GET'])
def getCandidatos():
    try:
        json = miControladorCandidato.index()
        return jsonify(json)
    except Exception as ex:
        return jsonify({'Ha ocurrido el siguiente error con el siguiente parametro':str(ex)})
@candidato.route("/candidatos",methods=['POST'])
def crearCandidato():
    try:
        data = request.get_json()
        json = miControladorCandidato.create(data)
        return jsonify(json)
    except Exception as ex:
        return jsonify({'Ha ocurrido el siguiente error con el siguiente parametro':str(ex)})
@candidato.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    try:
        json = miControladorCandidato.show(id)
        return jsonify(json)
    except Exception as ex:
        return jsonify({'ERROR - ID de candidato no valido o no encontrado, verifica el ID del candidato a buscar':str(ex)})
@candidato.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    try:
        data = request.get_json()
        json = miControladorCandidato.update(id, data)
        return jsonify(json)
    except Exception as ex:
        return jsonify({'ERROR - ID de Candidato no valido o no encontrado, verifica el ID del Candidato a buscar':str(ex)})

@candidato.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    try:
        json = miControladorCandidato.delete(id)
        return jsonify(json)
    except Exception as ex:
        return jsonify({'ERROR - ID de Candidato no valido o no encontrado, verifica el ID del Candidato a buscar':str(ex)})

@candidato.route("/candidatos/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoAlCandidato(id,id_partido):
    try:
        json = miControladorCandidato.asignarPartido(id, id_partido)
        return jsonify(json)
    except Exception as ex:
        return jsonify({'ERROR - Verificar los ID asignados de candidato o ID asignados de partido':str(ex)})
