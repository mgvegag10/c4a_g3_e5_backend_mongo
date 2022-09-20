from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson.son import SON
from bson import ObjectId

class RepositorioReporte(InterfaceRepositorio[Resultado]):

    def ListadoVotosEnMesas(self):
        query2 = {
            "$sort": {"participacion": 1}
        }
        query1 = {
            "$group": {
                "_id": "$mesa",
                "participacion": {
                    "$sum": "$cant_votos"
                }
            }
        }
        query3 ={
            "$lookup":{
                "from": "mesa",
                "localField": "mesa",
                "foreignField": "_id",
                "as":"mesa"
            }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)

    def ListadoVotosCandidatos(self):
        query1 = {
            "$group": {
                "_id": "$candidato",
                "votacion": {
                    "$sum": "$cant_votos"
                }
            }
        }
        query2 = {
            "$sort": {"participacion": -1}
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)

    def ListadoVotosCandidato(self, id_candidato):
        query ={
            "$match":{"candidato.$id": ObjectId(id_candidato)}
        }
        query1 = {
            "$group": {
                "_id": "$candidato",
                "votacion": {
                    "$sum": "$cant_votos"
                }
            }
        }
        query2 = {
            "$sort": {"participacion": -1}
        }
        pipeline = [query, query1, query2]
        return self.queryAggregation(pipeline)