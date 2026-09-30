from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, sessionmaker
from typing import List

from models import db, Base, Usuario
from schemas import UsuarioSchema
from routes.auth_routes import auth_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra as rotas do grupo
app.include_router(auth_routes)

@app.get("/")
def home():
    return {"mensagem": "API do IFuncao rodando com sucesso!"}
