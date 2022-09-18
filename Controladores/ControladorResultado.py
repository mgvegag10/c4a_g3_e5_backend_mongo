from flask import request
from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidatos = RepositorioCandidato()
        self.repositorioMesas = RepositorioMesa()

    def index(self):
        return self.repositorioResultado.findAll()

    """
        Asignacion mesa y candidato a resultado
    """

    def create(self,infoResultado,id_candidato,id_mesa):
        nuevoResultado = Resultado(infoResultado)
        elCandidato = Candidato(self.repositorioCandidatos.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesas.findById(id_mesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
        Modificación de resultado (mesa y candidato)
    """

    def update(self, id, infoResultado,id_candidato,id_mesa):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        elResultado.cant_votos = infoResultado["cant_votos"]
        elCandidato = Candidato(self.repositorioCandidatos.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesas.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)