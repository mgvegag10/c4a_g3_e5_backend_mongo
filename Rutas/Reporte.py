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
