from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioSchema(BaseModel):
    user_nome: str
    user_matricula: int
    user_email: str
    user_ano_letivo: Optional[str] = None
    user_curso: Optional[str] = None
    user_data_nascimento: Optional[date] = None
    user_foto_url: Optional[str] = None
    user_ofensiva_dias: int = 0

    class Config:
        from_attributes = True