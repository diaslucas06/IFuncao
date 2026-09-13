from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import requests

from models import Usuario
from schemas import UsuarioSchema, LoginSchema
from dependencies import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["auth"])

URL_SUAP_TOKEN = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/"
URL_SUAP_MEUS_DADOS = "https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/"

HEADERS_HTTP = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

@auth_router.post("/login", response_model=UsuarioSchema)
def login(dados_login: LoginSchema, db: Session = Depends(pegar_sessao)):
    payload = {
        "username": str(dados_login.user_matricula),
        "password": dados_login.user_senha
    }
    
    resposta_suap = requests.post(URL_SUAP_TOKEN, data=payload, headers=HEADERS_HTTP)

    if resposta_suap.status_code != 200:
        #print para ver o erro
        print("-> RESPOSTA DO SUAP:", resposta_suap.status_code, resposta_suap.text)
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Matrícula ou senha do SUAP incorretas."
        )

    token = resposta_suap.json().get("token")

    usuario = db.query(Usuario).filter(Usuario.user_matricula == dados_login.user_matricula).first()

    if not usuario:
        auth_headers = {
            "Authorization": f"JWT {token}",
            "User-Agent": HEADERS_HTTP["User-Agent"]
        }
        res_dados = requests.get(URL_SUAP_MEUS_DADOS, headers=auth_headers)
        dados_suap = res_dados.json() if res_dados.status_code == 200 else {}

        usuario = Usuario(
            user_nome=dados_suap.get("vinculo", {}).get("nome", dados_suap.get("nome_usual", "Aluno")),
            user_matricula=dados_login.user_matricula,
            user_email=dados_suap.get("email", ""),
            user_ano_letivo="1º Ano",
            user_curso=dados_suap.get("vinculo", {}).get("curso", ""),
            user_data_nascimento=None,
            user_foto_url=dados_suap.get("url_foto_150x200", ""),
            user_ofensiva_dias=0
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)

    return usuario