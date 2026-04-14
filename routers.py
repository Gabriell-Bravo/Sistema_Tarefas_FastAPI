from fastapi import APIRouter
from bson import ObjectId
from database import Tarefas_collection
from schemas import Tarefas

router = APIRouter()
# GET/todas as tarefas


@router.get("/tarefas")
def listar_tarefas():
    Tarefas_list = []

    for tarefa in Tarefas_collection.find():
        tarefa["_id"] = str(tarefa["_id"])
        Tarefas_list.append(tarefa)

    return Tarefas_list


@router.post("/cadastro_tarefas")
def Cadastro_Tarefas(tarefas: Tarefas):
    tarefas_dict = tarefas.model_dump()
    result = Tarefas_collection.insert_one(tarefas_dict)

    return {"message": "tarefa criada",
            "id": str(result.inserted_id)}


@router.delete("/deletar_tarefa/{_id}")
def deletar_tarefa(_id : str):
    filtro = {"_id": ObjectId(_id)}
    result = Tarefas_collection.delete_one(filtro)
    
    if result.deleted_count > 0:
        return {"message": "tarefa deletada", "id": _id}
    else:
        return {"message": "tarefa não encontrada"}
 
    
@router.put("/update/{_id}")
def tarefa_update(_id: str, tarefas: Tarefas):
        filtro = {"_id": ObjectId(_id)}
        tarefas_dict = tarefas.model_dump()   
        result = Tarefas_collection.update_one( filtro, {"$set": tarefas_dict})   
          
        return {"message": "tarefa atualizada", "id": _id} 
    