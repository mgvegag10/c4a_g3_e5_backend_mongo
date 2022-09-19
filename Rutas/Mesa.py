from flask import jsonify, Blueprint, request
from Controladores.ControladorMesa import ControladorMesa

miControladorMesa = ControladorMesa()

mesa = Blueprint('mesa',__name__)

@mesa.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)
@mesa.route("/mesas",methods=['POST'])
def crearMesa():
    try:
        data = request.get_json()
        json = miControladorMesa.create(data)
        return jsonify(json)
    except Exception as ex:
        return jsonify({'Ha ocurrido el siguiente error con el siguiente parametro':str(ex)})

@mesa.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    try:
        json=miControladorMesa.show(id)
        return jsonify(json)
    except Exception as ex:
        return jsonify({'ID de mesa no valido o no encontrado, verifica el ID de mesa buscar - ERROR ':str(ex)})
@mesa.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    try:
        data = request.get_json()
        json=miControladorMesa.update(id,data)
        return jsonify(json)
    except Exception as ex:
        return jsonify({'Ha ocurrido el siguiente error con el siguiente parametro':str(ex)})

@mesa.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    try:
        json = miControladorMesa.delete(id)
        return jsonify(json)
    except Exception as ex:
        return jsonify({'Ha ocurrido el siguiente error con el siguiente parametro':str(ex)})