from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
import unicodedata
from datetime import timedelta, date

from config import ALGORITHM, SECRET_KEY
from models import db, Usuario
from sqlalchemy.orm import sessionmaker

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session

    finally:
        session.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def pegar_usuario_logado(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(pegar_sessao)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

    usuario = db.query(Usuario).filter(Usuario.user_id == int(user_id)).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return usuario

def normalizar_texto(texto: str) -> str:
    # Tira acentos e deixa em minúsculo
    sem_acento = "".join(
        c for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )
    return sem_acento.lower().strip()

def calcular_ofensiva(dias: set[date]) -> int:
    hoje = date.today()
    dia = hoje if hoje in dias else hoje - timedelta(days=1)

    ofensiva = 0
    while dia in dias:
        ofensiva += 1
        dia -= timedelta(days=1)
    return ofensiva