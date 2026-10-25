from pydantic import BaseModel
from typing import Optional, Dict
from datetime import date, datetime

class UsuarioSchema(BaseModel):
    user_nome: str
    user_matricula: int
    user_email: str
    user_ano_letivo: Optional[str] = None
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
    perfil_nome: str
    perfil_matricula: int
    perfil_ano_letivo: Optional[str] = None
    perfil_email: str
    perfil_curso: Optional[str] = None
    perfil_data_nascimento: Optional[date] = None
    perfil_progresso: Optional[str] = None
    perfil_mediageral: Optional[float] = None
    perfil_foto_url: Optional[str] = None

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
    respquest_ques_id: int
    respquest_alternativa_escolhida: str