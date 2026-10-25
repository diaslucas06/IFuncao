from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models import Conteudo, UsuarioConteudo, Usuario
from schemas import ConteudoSchema
from dependencies import pegar_sessao, pegar_usuario_logado

conteudos_routes = APIRouter(prefix="/conteudos", tags=["Conteúdos"])

@conteudos_routes.get("/{cont_nome}", response_model=ConteudoSchema)
async def listar_conteudo(
    cont_nome: str, 
    db: Session = Depends(pegar_sessao),
    # usuario: Usuario = Depends(pegar_usuario_logado)
):
    # Busca o conteudo vinculado ao título informado
    conteudo = db.query(Conteudo).filter(Conteudo.cont_nome == cont_nome).first()
    
    if not conteudo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum conteúdo encontrado com este título."
        )
        
    return conteudo