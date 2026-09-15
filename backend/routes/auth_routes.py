from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date
import httpx

# Ajuste os imports abaixo de acordo com os arquivos do seu projeto
from models import Usuario
from schemas import LoginSchema, UsuarioSchema
from dependencies import pegar_sessao  # Assumindo que você tem essa função que gera a sessão do DB

auth_routes = APIRouter(prefix="/auth", tags=["Autenticação"])

URL_TOKEN = "https://suap.ifrn.edu.br/api/token/pair"
URL_MEUS_DADOS = "https://suap.ifrn.edu.br/api/ensino/meus-dados-aluno/"
URL_RH_EU = "https://suap.ifrn.edu.br/api/rh/eu/"
HEADERS_PADRAO = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

@auth_routes.post("/login", response_model=UsuarioSchema)
async def login(dados_login: LoginSchema, db: Session = Depends(pegar_sessao)):
    
    # 1. Tenta autenticar no SUAP
    async with httpx.AsyncClient() as client:
        resposta_token = await client.post(
            URL_TOKEN,
            json={"username": str(dados_login.user_matricula), "password": dados_login.user_senha},
            headers=HEADERS_PADRAO
        )

        if resposta_token.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Matrícula ou senha do SUAP incorretas."
            )

        token = resposta_token.json().get("access")

        # 2. Verifica se o aluno já existe no NOSSO banco de dados do IFunção
        usuario = db.query(Usuario).filter(Usuario.user_matricula == dados_login.user_matricula).first()

        if usuario:
            headers_auth = {
                "Authorization": f"Bearer {token}",
                **HEADERS_PADRAO
            }
            resposta_dados = await client.get(URL_MEUS_DADOS, headers=headers_auth)

            if resposta_dados.status_code == 200:
                dados_suap = resposta_dados.json()
                resposta_perfil = await client.get(URL_RH_EU, headers=headers_auth)
                dados_perfil = resposta_perfil.json() if resposta_perfil.status_code == 200 else {}
                data_nascimento = dados_perfil.get("data_de_nascimento")
                usuario.user_email = dados_suap.get("email_academico") or dados_suap.get("email_escolar") or usuario.user_email
                usuario.user_curso = dados_suap.get("curso") or usuario.user_curso
                usuario.user_nome = dados_perfil.get("nome_usual") or dados_perfil.get("nome") or usuario.user_nome
                usuario.user_foto_url = dados_perfil.get("foto") or usuario.user_foto_url
                if data_nascimento:
                    usuario.user_data_nascimento = date.fromisoformat(data_nascimento)
                db.commit()
                db.refresh(usuario)

            return usuario

        # 3. Se não existir, busca os dados completos no SUAP para criar a conta
        if not usuario:
            headers_auth = {
                "Authorization": f"Bearer {token}",
                **HEADERS_PADRAO
            }
            
            resposta_dados = await client.get(URL_MEUS_DADOS, headers=headers_auth)
            
            # Fallback para JWT caso o Bearer falhe
            if resposta_dados.status_code == 401:
                headers_auth["Authorization"] = f"JWT {token}"
                resposta_dados = await client.get(URL_MEUS_DADOS, headers=headers_auth)
            
            if resposta_dados.status_code != 200:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Erro ao buscar os dados do aluno no SUAP."
                )

            dados_suap = resposta_dados.json()
            resposta_perfil = await client.get(URL_RH_EU, headers=headers_auth)
            dados_perfil = resposta_perfil.json() if resposta_perfil.status_code == 200 else {}
            data_nascimento = dados_perfil.get("data_de_nascimento")

            # Cria o usuário mapeando as chaves retornadas da API de ensino
            usuario = Usuario(
                user_nome=dados_perfil.get("nome_usual") or dados_perfil.get("nome") or "Aluno",
                user_matricula=dados_login.user_matricula,
                user_email=dados_suap.get("email_academico") or dados_suap.get("email_escolar") or "",
                user_ano_letivo="1º Ano", 
                user_curso=dados_suap.get("curso", ""),
                user_data_nascimento=date.fromisoformat(data_nascimento) if data_nascimento else None,
                user_foto_url=dados_perfil.get("foto", ""),
                user_ofensiva_dias=0
            )
            
            db.add(usuario)
            db.commit()
            db.refresh(usuario)

        # Retorna o usuário (o FastAPI usará o UsuarioSchema para formatar a saída automaticamente)
        print(dados_suap)
        return usuario