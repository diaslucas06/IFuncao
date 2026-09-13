from pydantic import BaseModel
from typing import Optional
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