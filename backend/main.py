from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session, sessionmaker
from typing import List

from models import db, Base, Usuario
from schemas import UsuarioSchema

app = FastAPI(title="IFuncao API")

@app.get("/")
def home():
    return {"mensagem": "API do IFuncao rodando com sucesso!"}
