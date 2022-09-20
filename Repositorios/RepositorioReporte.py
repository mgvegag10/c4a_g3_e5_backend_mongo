from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId

class RepositorioReporte(InterfaceRepositorio[Resultado]):

    def ListadoVotosEnMesas(self):
        query1 = {
            "$group": {
                "_id": "$mesa",
                "participacion": {
                    "$sum": "$cant_votos"
                }
            }
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)