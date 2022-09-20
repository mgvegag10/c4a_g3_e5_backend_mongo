from flask import request
from Modelos.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido


class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioPartido.findAll()

    def create(self, infoPartido):
        # Solicita los datos de la llave en el JSON
        nombre = infoPartido['nombre']
        lema = infoPartido['lema']
        partidos = self.repositorioPartido.findAll()

        # Validación de datos
        for partido in partidos:
            if partido['nombre'] == nombre:
                raise ValueError(" ERROR - El nombre del partido ya se encuentra en la base de datos")
        if (len(infoPartido) > 2):
            raise ValueError("Cantidad de argumentos invalidos")
        if ("nombre" and "lema") in infoPartido:
            nuevoPartido = Partido(infoPartido)
            return self.repositorioPartido.save(nuevoPartido)
        else:
            raise ValueError("Faltan argumentos")

    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido):
        partidoActual = Partido(self.repositorioPartido.findById(id))
        if ("nombre" and "lema") in infoPartido:
            partidoActual.nombre = infoPartido["nombre"]
            partidoActual.lema = infoPartido["lema"]
            return self.repositorioPartido.save(partidoActual)
        else:
            raise ValueError("Faltan argumentos")

    def delete(self, id):
        return self.repositorioPartido.delete(id)