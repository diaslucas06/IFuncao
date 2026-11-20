from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models import Questao, Simulado, Usuario, EtapaEnum
from schemas import (
    SimuladoIniciarResponse,
    SimuladoFinalizarRequest,
    SimuladoResultadoResponse,
    SimuladoHistoricoItem,
)
from dependencies import pegar_sessao, pegar_usuario_logado

simulados_routes = APIRouter(prefix="/simulados", tags=["Simulados"])


@simulados_routes.get("/iniciar", response_model=SimuladoIniciarResponse)
async def iniciar_simulado(
    etapa: EtapaEnum = EtapaEnum.ETAPA_1,
    db: Session = Depends(pegar_sessao),
):
    questoes = (
        db.query(Questao)
        .filter(Questao.ques_cont_id.is_(None), Questao.ques_etapa == etapa)
        .order_by(Questao.ques_id.asc())
        .all()
    )

    if not questoes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nenhuma questão de simulado encontrada para a etapa {etapa.value}."
        )

    return {
        "etapa": etapa,
        "total_questoes": len(questoes),
        "questoes": questoes,
    }


@simulados_routes.post("/finalizar", response_model=SimuladoResultadoResponse)
async def finalizar_simulado(
    dados: SimuladoFinalizarRequest,
    db: Session = Depends(pegar_sessao),
    usuario: Usuario = Depends(pegar_usuario_logado),
):
    questoes = (
        db.query(Questao)
        .filter(Questao.ques_cont_id.is_(None), Questao.ques_etapa == dados.etapa)
        .order_by(Questao.ques_id.asc())
        .all()
    )

    if not questoes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Simulado não encontrado para esta etapa."
        )

    mapa_respostas = {
        item.ques_id: (item.alternativa_escolhida.value if item.alternativa_escolhida else None)
        for item in dados.respostas
    }

    acertos = 0
    detalhes_lista = []

    for q in questoes:
        escolhida = mapa_respostas.get(q.ques_id)
        correta = (
            q.ques_resposta_correta.value
            if hasattr(q.ques_resposta_correta, "value")
            else str(q.ques_resposta_correta).strip().upper()
        )
        acertou = (escolhida == correta)
        if acertou:
            acertos += 1

        detalhes_lista.append({
            "ques_id": q.ques_id,
            "ques_enunciado": q.ques_enunciado,
            "ques_imagem_url": q.ques_imagem_url,
            "alternativa_escolhida": escolhida,
            "resposta_correta": correta,
            "acertou": acertou,
            "ques_resolucao": q.ques_resolucao,
            "ques_resolucao_imagem_url": q.ques_resolucao_imagem_url,
        })

    total_questoes = len(questoes)
    nota = round((acertos / total_questoes) * 1000) if total_questoes > 0 else 0

    novo_simulado = Simulado(
        sim_user_id=usuario.user_id,
        sim_etapa=dados.etapa,
        sim_total_questoes=total_questoes,
        sim_acertos=acertos,
        sim_nota=nota,
        sim_detalhes_respostas={"detalhes": detalhes_lista},
    )

    db.add(novo_simulado)
    db.commit()
    db.refresh(novo_simulado)

    return {
        "sim_id": novo_simulado.sim_id,
        "sim_etapa": novo_simulado.sim_etapa,
        "sim_total_questoes": novo_simulado.sim_total_questoes,
        "sim_acertos": novo_simulado.sim_acertos,
        "sim_nota": novo_simulado.sim_nota,
        "sim_data_realizacao": novo_simulado.sim_data_realizacao,
        "detalhes": detalhes_lista,
    }


@simulados_routes.get("/historico", response_model=List[SimuladoHistoricoItem])
async def historico_simulados(
    db: Session = Depends(pegar_sessao),
    usuario: Usuario = Depends(pegar_usuario_logado),
):
    simulados = (
        db.query(Simulado)
        .filter(Simulado.sim_user_id == usuario.user_id)
        .order_by(Simulado.sim_data_realizacao.desc())
        .all()
    )
    return simulados