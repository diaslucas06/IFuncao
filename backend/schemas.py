from pydantic import BaseModel
from typing import Optional, Dict, Union, List
from datetime import date, datetime
from models import AlternativaEnum, EtapaEnum, DificuldadeEnum

class UsuarioSchema(BaseModel):
    user_nome: str
    user_matricula: int
    user_email: str
    user_ano_letivo: Optional[Union[int, str]] = None
    user_curso: Optional[str] = None
    user_data_nascimento: Optional[date] = None
    user_foto_url: Optional[str] = None

    class Config:
        from_attributes = True

class AcessoSchema(BaseModel):
    ace_user_id: int
    ace_data: date
    ace_hora_inicio: datetime
    ace_hora_fim: datetime
    
class LoginSchema(BaseModel):
    user_matricula: int
    user_senha: str

class LoginResponseSchema(BaseModel):
    usuario: UsuarioSchema
    access_token: str
    refresh_token: str
    token_type: str

    class Config:
        from_attributes = True
        
class PerfilSchema(BaseModel):
    user_id: int
    user_nome: str
    user_matricula: int
    user_email: str
    user_ano_letivo: Optional[Union[int, str]] = None
    user_curso: Optional[str] = None
    user_data_nascimento: Optional[date] = None
    user_foto_url: Optional[str] = None

    class Config:
        from_attributes = True


class ConteudoSchema(BaseModel):
    cont_id: int
    cont_nome: str
    cont_etapa: Dict[str, str]
    cont_texto: str
    cont_texto_resumo: str
    cont_slide_pdf: Optional[str] = None
    cont_relacionados: Dict[str, str]

    class Config:
        from_attributes = True
    
class QuestaoSchema(BaseModel):
    ques_id: int
    ques_cont_id: int
    ques_enunciado: str
    ques_imagem_url: Optional[str] = None
    ques_alternativas: Dict[str, str]

    class Config:
        from_attributes = True

class RespostaSchema(BaseModel):
    respques_ques_id: int
    respques_alternativa_escolhida: AlternativaEnum
    
class QuestaoSimuladoSchema(BaseModel):
    ques_id: int
    ques_enunciado: str
    ques_imagem_url: Optional[str] = None
    ques_alternativas: Dict[str, str]
    ques_etapa: EtapaEnum
    ques_nivel_dificuldade: DificuldadeEnum

    class Config:
        from_attributes = True

class SimuladoIniciarResponse(BaseModel):
    etapa: EtapaEnum
    total_questoes: int
    questoes: List[QuestaoSimuladoSchema]

class RespostaItemSimulado(BaseModel):
    ques_id: int
    alternativa_escolhida: Optional[AlternativaEnum] = None

class SimuladoFinalizarRequest(BaseModel):
    etapa: EtapaEnum = EtapaEnum.ETAPA_1
    respostas: List[RespostaItemSimulado]

class DetalheCorrecaoQuestao(BaseModel):
    ques_id: int
    ques_enunciado: str
    ques_imagem_url: Optional[str] = None
    alternativa_escolhida: Optional[str] = None
    resposta_correta: str
    acertou: bool
    ques_resolucao: Optional[str] = None
    ques_resolucao_imagem_url: Optional[str] = None

class SimuladoResultadoResponse(BaseModel):
    sim_id: int
    sim_etapa: EtapaEnum
    sim_total_questoes: int
    sim_acertos: int
    sim_nota: int
    sim_data_realizacao: datetime
    detalhes: List[DetalheCorrecaoQuestao]

    class Config:
        from_attributes = True

class SimuladoHistoricoItem(BaseModel):
    sim_id: int
    sim_etapa: EtapaEnum
    sim_total_questoes: int
    sim_acertos: int
    sim_nota: int
    sim_data_realizacao: datetime

    class Config:
        from_attributes = True

class ConteudoResponse(BaseModel):
    cont_id: int
    cont_nome: str
    cont_etapa: str

    class Config:
        from_attributes = True

