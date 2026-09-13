from fastapi import APIRouter, Depends
from models import Usuario
from schemas import UsuarioSchema, AcessoSchema # Podem ignorar o de acesso por enquanto, foquem no login puro
from dependencies import pegar_sessao
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

# Acredito que haja tudo que é necessário pra fazer a rota de login, menos o negócio pronto né
