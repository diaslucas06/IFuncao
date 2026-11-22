from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from datetime import datetime, timezone
from urllib.parse import unquote
from typing import List

from models import Conteudo, UsuarioConteudo, Usuario, EtapaEnum
from schemas import ConteudoSchema, ConteudoResponse
from dependencies import pegar_sessao, pegar_usuario_logado, normalizar_texto

conteudos_routes = APIRouter(prefix="/conteudos", tags=["Conteúdos"])

@conteudos_routes.get("/buscar", response_model=List[ConteudoResponse])
def buscar_conteudos(
    q: str = Query(..., min_length=2, description="Parte do nome do conteúdo"),
    limite: int = Query(20, ge=1, le=100),
    db: Session = Depends(pegar_sessao),
):
    palavras = normalizar_texto(unquote(q)).split()

    if not palavras:
        return []

    conteudos = db.query(
        Conteudo.cont_id,
        Conteudo.cont_nome,
        Conteudo.cont_etapa,
    ).all()

    resultados = []
    for c in conteudos:
        nome = normalizar_texto(c.cont_nome)
        if all(p in nome for p in palavras):
            resultados.append((c, nome))

    termo = " ".join(palavras)
    resultados.sort(key=lambda r: (not r[1].startswith(termo), r[1]))

    return [c for c, _ in resultados[:limite]]

@conteudos_routes.get("/buscar/{cont_etapa}", response_model=List[ConteudoResponse])
def buscar_conteudos_etapa(
    cont_etapa: EtapaEnum,
    q: str = Query(..., min_length=2, description="Parte do nome do conteúdo"),
    limite: int = Query(20, ge=1, le=100),
    db: Session = Depends(pegar_sessao),
):
    palavras = normalizar_texto(unquote(q)).split()

    if not palavras:
        return []

    conteudos = db.query(
        Conteudo.cont_id,
        Conteudo.cont_nome,
        Conteudo.cont_etapa,
    ).filter(Conteudo.cont_etapa == cont_etapa).all()

    resultados = []
    for c in conteudos:
        nome = normalizar_texto(c.cont_nome)
        if all(p in nome for p in palavras):
            resultados.append((c, nome))

    termo = " ".join(palavras)
    resultados.sort(key=lambda r: (not r[1].startswith(termo), r[1]))

    return [c for c, _ in resultados[:limite]]

@conteudos_routes.get("/historico", response_model=List[ConteudoResponse])
def listar_historico(
    limite: int = Query(10, ge=1, le=20),
    db: Session = Depends(pegar_sessao),
    usuario: Usuario = Depends(pegar_usuario_logado),
):
    return (
        db.query(Conteudo)
        .join(UsuarioConteudo, UsuarioConteudo.usercont_cont_id == Conteudo.cont_id)
        .filter(UsuarioConteudo.usercont_user_id == usuario.user_id)
        .group_by(Conteudo.cont_id)
        .order_by(func.max(UsuarioConteudo.usercont_ultimo_acesso).desc())
        .limit(limite)
        .all()
    )

@conteudos_routes.get("/{cont_etapa}")
async def conteudos_etapa(
    cont_etapa: str,
    db: Session = Depends(pegar_sessao),
):
    conteudos = db.query(Conteudo).filter(Conteudo.cont_etapa == cont_etapa).all()

    if not conteudos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum conteúdo encontrado para essa etapa."
        )
    
    return conteudos

@conteudos_routes.get("/{cont_etapa}/{cont_nome}", response_model=ConteudoSchema)
async def listar_conteudo(
    cont_nome: str, 
    db: Session = Depends(pegar_sessao),
    usuario: Usuario = Depends(pegar_usuario_logado)
):
    # Busca o conteudo vinculado ao título informado
    conteudo = db.query(Conteudo).filter(Conteudo.cont_nome == cont_nome).first()
    
    if not conteudo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum conteúdo encontrado com este título."
        )
    
    usuario_conteudo = db.query(UsuarioConteudo).filter(UsuarioConteudo.usercont_user_id == usuario.user_id, UsuarioConteudo.usercont_cont_id == conteudo.cont_id).first()
        
    atual = datetime.now(timezone.utc)

    if usuario_conteudo:
        usuario_conteudo.usercont_ultimo_acesso = atual
    
    else:     
        usuario_conteudo = UsuarioConteudo(
            usercont_user_id = usuario.user_id,
            usercont_cont_id = conteudo.cont_id,
            usercont_ultimo_acesso = atual
        )
        db.add(usuario_conteudo)
    
    
    db.commit()
    db.refresh(conteudo)
    return conteudo

