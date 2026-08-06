from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session, sessionmaker
from typing import List

from models import db, Base, Usuario
from schemas import UsuarioSchema

# Cria as tabelas no banco.db se não existirem
Base.metadata.create_all(bind=db)

# Configura a conexão com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db)

app = FastAPI(title="IFuncao API")

# Função para conectar ao banco em cada requisição
def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

@app.get("/")
def home():
    return {"mensagem": "API do IFuncao rodando com sucesso!"}

# Rota para listar os usuários do banco
@app.get("/usuarios", response_model=List[UsuarioSchema])
def listar_usuarios(db_session: Session = Depends(get_db)):
    return db_session.query(Usuario).all()