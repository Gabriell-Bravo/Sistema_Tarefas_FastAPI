from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27018"

client = MongoClient(MONGO_URL)

db = client["ATV_P1"]

Tarefas_collection = db["Tarefas"]