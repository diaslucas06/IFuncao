from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models import Questao, RespostaQuestao, Usuario, AlternativaEnum
from schemas import QuestaoSchema, RespostaSchema
from dependencies import pegar_sessao, pegar_usuario_logado

questoes_routes = APIRouter(prefix="/questoes", tags=["Questões"])

@questoes_routes.get("/conteudo/{cont_id}", response_model=list[QuestaoSchema])
async def listar_questoes_por_conteudo(
    cont_id: int, 
    db: Session = Depends(pegar_sessao),
    # usuario: Usuario = Depends(pegar_usuario_logado)
):
    # Busca todas as questões vinculadas ao conteúdo informado
    questoes = db.query(Questao).filter(Questao.ques_cont_id == cont_id).all()
    
    if not questoes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma questão encontrada para este conteúdo."
        )
        
    return questoes

@questoes_routes.post("/responder")
async def responder_questao(
    dados: RespostaSchema, 
    db: Session = Depends(pegar_sessao),
    usuario: Usuario = Depends(pegar_usuario_logado)
):
    # Verifica se a questão existe no banco
    questao = db.query(Questao).filter(Questao.ques_id == dados.respques_ques_id).first()
    
    if not questao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Questão não encontrada."
        )
    
    # Extrai o valor string ("A", "B", "C", "D" ou "E") tanto do schema quanto do banco
    escolhida = dados.respques_alternativa_escolhida.value
    correta = (
        questao.ques_resposta_correta.value
        if hasattr(questao.ques_resposta_correta, "value")
        else str(questao.ques_resposta_correta).strip().upper()
    )
    
    # Booleano True ou False
    acertou = (escolhida == correta)
    
    # Registra a tentativa do aluno
    nova_resposta = RespostaQuestao(
        respques_user_id=usuario.user_id,
        respques_ques_id=questao.ques_id,
        respques_alternativa_escolhida=AlternativaEnum(escolhida),
        respques_acertou=acertou
    )
    
    db.add(nova_resposta)
    db.commit()
    db.refresh(nova_resposta)
    
    return {
        "mensagem": "Resposta registrada com sucesso!",
        "acertou": acertou,
        "alternativa_escolhida": escolhida,
        "resposta_correta": correta
    }