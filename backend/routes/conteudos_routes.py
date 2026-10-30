from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from models import Conteudo, UsuarioConteudo, Usuario
from schemas import ConteudoSchema
from dependencies import pegar_sessao, pegar_usuario_logado

conteudos_routes = APIRouter(prefix="/conteudos", tags=["Conteúdos"])

@conteudos_routes.get("/{cont_nome}", response_model=ConteudoSchema)
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