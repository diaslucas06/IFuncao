from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session, sessionmaker
from typing import List

from models import db, Base, Usuario
from schemas import UsuarioSchema
from routes.auth_routes import auth_router

app = FastAPI(title="IFuncao API")

# Registra as rotas do grupo
app.include_router(auth_router)

@app.get("/")
def home():
    return {"mensagem": "API do IFuncao rodando com sucesso!"}
