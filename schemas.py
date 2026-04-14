from pydantic import BaseModel

class Tarefas(BaseModel):
    nome : str
    horario : int
    prioridade : str