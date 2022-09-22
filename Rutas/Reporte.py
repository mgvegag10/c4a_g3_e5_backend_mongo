from flask import jsonify, Blueprint, request, Response
from Controladores.ControladorResultado import ControladorResultado

miControladorResultado = ControladorResultado()

reporte = Blueprint('reporte',__name__)

@reporte.route("/reportes/votos_mesas",methods=['GET'])
def getListadoVotosEnMesas():
    try:
        json=miControladorResultado.ListadoVotosEnMesas()
        return jsonify(json),200
    except Exception as e:
        strE = format(e)
        return jsonify('Ha ocurrido el siguiente error : ' + strE), 500

@reporte.route("/reportes/votos_candidatos",methods=['GET'])
def getListadoVotosCandidatos():
    try:
        json=miControladorResultado.ListadoVotosCandidatos()
        return jsonify(json),200
    except Exception as e:
        strE = format(e)
        return jsonify('Ha ocurrido el siguiente error : ' + strE), 500

@reporte.route("/reportes/votos_candidatos/candidato/<string:id_candidato>",methods=['GET'])
def getListadoVotosCandidato(id_candidato):
    try:
        json=miControladorResultado.ListadoVotosCandidato(id_candidato)
        return jsonify(json),200
    except Exception as e:
        strE = format(e)
        if strE.__contains__('keys'):
            return jsonify('Ha ocurrido el siguiente error : El id del candidato no existe'), 400
        else:
            return jsonify('Ha ocurrido el siguiente error : ' + strE), 500


@reporte.route("/reportes/votos_partidos",methods=['GET'])
def getListadoPartidosVotos():
    try:
        json=miControladorResultado.ListadoPartidosVotos()
        return jsonify(json),200
    except Exception as e:
        strE = format(e)
        return jsonify('Ha ocurrido el siguiente error : ' + strE), 500
