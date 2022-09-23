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
    
    def ListadoPartidosVotos(self,id_mesa=""):

      
        query1={
            "$lookup":{"from":"candidato","localField":"candidato.$id","foreignField":"_id","as":"resultado"}
        }
        query2={
           "$unwind":"$resultado"    
        }

        query4={
            "$lookup":{"from":"partido","localField":"resultado.partido.$id","foreignField":"_id","as":"resultado2"}
        }    

        query5={
           "$unwind":"$resultado2"    
        }
      
      
        query7={
                "$group":{
                "_id": {"id":"$resultado2._id", "nombre":"$resultado2.nombre"},
                "votacion":{
                    "$sum":"$cant_votos"
                },
                

            }
        }
        
        query8={
            "$sort": {"votacion": -1}
            }

        if (id_mesa != ""):
            query6 ={
            "$match":{"mesa.$id": ObjectId(id_mesa)}
            }
        
            pipeline = [query1,query2,query4,query5,query6,query7,query8]
            return self.queryAggregation(pipeline)
      
        else :
            pipeline = [query1,query2,query4,query5,query7,query8]
        
      
        
        return self.queryAggregation(pipeline)