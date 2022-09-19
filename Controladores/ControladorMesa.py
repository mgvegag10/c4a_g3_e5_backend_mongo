from flask import request, jsonify
from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        #Solicita los datos de la llave en el JSON
        numero = infoMesa['numero']
        cantidadInscritos = infoMesa['cantidadInscritos']
        mesas = self.repositorioMesa.findAll()

        #Validación de datos
        for mesa in mesas:
            if mesa['numero']==numero:
                return ' ERROR - El nombre de la mesa se repite'

        if numero == "" or cantidadInscritos == "":
            return 'ERROR - Alguno de los parametros está vacio'
        else:
            # Crea la mesa
            nuevaMesa = Mesa(infoMesa)
            return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesa):
        #Solicita los datos de la llave en el JSON
        numero = request.json['numero']
        cantidadInscritos = request.json['cantidadInscritos']

        #Actualiza los datos
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero = infoMesa["numero"]
        mesaActual.cant_inscritos = infoMesa["cantidadInscritos"]
        return self.repositorioMesa.save(mesaActual)

    def delete(self, id):
        return self.repositorioMesa.delete(id)


