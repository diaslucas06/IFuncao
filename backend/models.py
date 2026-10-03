from typing import Optional
from datetime import date, datetime

from sqlalchemy import create_engine, String, Integer, ForeignKey, Date, Text, JSON, DateTime, Enum, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

db = create_engine("sqlite:///banco.db")


class Base(DeclarativeBase):
    pass

class Usuario(Base):

    __tablename__ = "usuarios" 

    __table_args__ = (
        CheckConstraint("user_ano_letivo BETWEEN 1 AND 4", name="ck_user_ano_letivo"),
    )

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_nome: Mapped[str] = mapped_column(String(80))
    user_matricula: Mapped[int] = mapped_column(unique=True)
    user_email: Mapped[str] = mapped_column(String(100), unique=True)
    user_ano_letivo: Mapped[Optional[int]] = mapped_column(Integer)
    user_curso: Mapped[Optional[str]] = mapped_column(String(30))
    user_data_nascimento: Mapped[Optional[date]] = mapped_column(Date)
    user_foto_url: Mapped[Optional[str]] = mapped_column(String(100))
    user_progresso: Mapped[dict] = mapped_column(JSON)
    user_media_matematica: Mapped[Optional[float]]

class Acesso(Base):

    __tablename__ = "acessos"

    ace_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ace_user_id: Mapped[int] = mapped_column(ForeignKey('usuarios.user_id'))
    ace_hora_inicio: Mapped[datetime] = mapped_column(DateTime)
    ace_hora_fim: Mapped[Optional[datetime]] = mapped_column(DateTime)

class Questao(Base):

    __tablename__ = "questoes" 

    ques_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ques_cont_id: Mapped[int] = mapped_column(ForeignKey('conteudos.cont_id'))
    ques_enunciado: Mapped[str] = mapped_column(Text)
    ques_alternativas: Mapped[dict] = mapped_column(JSON)
    ques_etapa: Mapped[str] = mapped_column(Enum("1", "2", "3", "ENEM", name="etapa_enum"))
    ques_nivel_dificuldade: Mapped[str] = mapped_column(Enum("Fácil", "Médio", "Difícil", name="nivel_dificuldade_enum"))
    ques_resposta_correta: Mapped[str] = mapped_column(Enum("A", "B", "C", "D", "E", name="alternativa_enum"))

class Conteudo(Base):

    __tablename__ = "conteudos" 

    cont_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cont_nome: Mapped[str] = mapped_column(String(30))
    cont_etapa: Mapped[str] = mapped_column(Enum("1", "2", "3", "ENEM", name="etapa_enum"))
    cont_slide_pdf: Mapped[str] = mapped_column(String(255))

class Usuario_Conteudo(Base):

    __tablename__ = "usuario_conteudos" 

    __table_args__ = (
        UniqueConstraint("usercont_user_id", "usercont_cont_id", name="uq_user_conteudo"),
    )

    usercont_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    usercont_user_id: Mapped[int] = mapped_column(ForeignKey('usuarios.user_id'))
    usercont_cont_id: Mapped[int] = mapped_column(ForeignKey('conteudos.cont_id'))
    usercont_concluido: Mapped[bool] = mapped_column(default=False)
    usercont_ultimo_acesso: Mapped[Optional[datetime]] = mapped_column(DateTime)

class Resposta_Questao(Base):

    __tablename__ = "resposta_questoes" 

    respques_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    respques_user_id: Mapped[int] = mapped_column(ForeignKey('usuarios.user_id'))
    respques_ques_id: Mapped[int] = mapped_column(ForeignKey('questoes.ques_id'))
    respques_alternativa_escolhida: Mapped[str] = mapped_column(Enum("A", "B", "C", "D", "E", name="alternativa_enum"))
    respques_acertou: Mapped[bool]
