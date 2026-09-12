from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, Date, Text, JSON, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///banco.db")

Base = declarative_base()

class Usuario(Base):

    __tablename__ = "usuarios" 

    user_id = Column('user_id', Integer, primary_key=True, autoincrement=True, )
    user_nome = Column('user_nome', String)
    user_matricula = Column('user_matricula', Integer, unique=True, nullable=False)
    user_email = Column('user_email', String)
    user_ano_letivo = Column('user_ano_letivo', String)
    user_curso = Column('user_curso', String)
    user_data_nascimento = Column('user_data_nascimento', Date)
    user_foto_url = Column('user_foto_url', String)
    user_ofensiva_dias = Column('user_ofensiva_dias', Integer)

    def __init__(self, user_nome, user_matricula, user_email, user_ano_letivo, user_curso, user_data_nascimento, user_foto_url, user_ofensiva_dias):
        self.user_nome = user_nome
        self.user_matricula = user_matricula
        self.user_email = user_email
        self.user_ano_letivo = user_ano_letivo
        self.user_curso = user_curso
        self.user_data_nascimento = user_data_nascimento
        self.user_foto_url = user_foto_url

class Acesso(Base):

    __tablename__ = "acessos"

    ace_id = Column('ace_id', Integer, primary_key=True, autoincrement=True)
    ace_user_id = Column('ace_user_id', ForeignKey('usuarios.user_id'))
    ace_data = Column('ace_data', Date)
    ace_hora_inicio = Column('ace_hora_inicio', DateTime)
    ace_hora_fim = Column('ace_hora_fim', DateTime)

class Questao(Base):

    __tablename__ = "questoes" 

    ques_id = Column('ques_id', Integer, primary_key=True, autoincrement=True)
    ques_enunciado = Column('ques_enunciado', Text)
    ques_alternativas = Column('ques_alternativas', JSON)
    ques_etapa = Column('ques_etapa', String)
    ques_nivel_dificuldade = Column('ques_nivel_dificuldade', String)
    ques_cont_id = Column('ques_cont_id', ForeignKey('conteudos.cont_id'))
    ques_resposta_correta = Column('ques_resposta_correta', String)
    

    def __init__(self, ques_enunciado, ques_alternativas, ques_etapa, ques_nivel_dificuldade, ques_cont_id, ques_resposta_correta):
        self.ques_enunciado = ques_enunciado
        self.ques_alternativas = ques_alternativas
        self.ques_etapa = ques_etapa
        self.ques_nivel_dificuldade = ques_nivel_dificuldade 
        self.ques_cont_id = ques_cont_id
        self.ques_resposta_correta = ques_resposta_correta

class Conteudo(Base):

    __tablename__ = "conteudos" 

    cont_id = Column('cont_id', Integer, primary_key=True, autoincrement=True)
    cont_nome = Column('cont_nome', String)
    cont_etapa = Column('cont_etapa', String)
    cont_slide_pdf = Column('cont_slide_pdf', String)

    def __init__(self, cont_nome, cont_etapa):
        self.cont_nome = cont_nome
        self.cont_etapa = cont_etapa

class Usuario_Conteudo(Base):

    __tablename__ = "usuario_conteudos" 

    usercont_id = Column('user_id', Integer, primary_key=True, autoincrement=True)
    usercont_user_id = Column('usercont_user_id', ForeignKey('usuarios.user_id'))
    usercont_cont_id = Column('usercont_cont_id', ForeignKey('conteudos.cont_id'))
    usercont_concluido = Column('usercont_concluido', Boolean)

    def __init__(self, usercont_user_id, usercont_cont_id, usercont_concluido):
        self.usercont_user_id = usercont_user_id
        self.usercont_cont_id = usercont_cont_id
        self.usercont_concluido = usercont_concluido

class Resposta_Questao(Base):

    __tablename__ = "resposta_questoes" 

    respques_id = Column('respques_id', Integer, primary_key=True, autoincrement=True)
    respques_user_id = Column('respques_user_id', ForeignKey('usuarios.user_id'))
    respques_ques_id = Column('respques_ques_id', ForeignKey('questoes.ques_id'))
    respques_alternativa_escolhida = Column('respques_alternativa_escolhida', String)
    respques_acertou = Column('respques_acertou', Boolean)
    

    def __init__(self, respques_user_id, respques_ques_id, respques_alternativa_escolhida, respques_acertou):
        self.respques_user_id = respques_user_id
        self.respques_ques_id = respques_ques_id
        self.respques_alternativa_escolhida = respques_alternativa_escolhida
        self.respques_acertou = respques_acertou

