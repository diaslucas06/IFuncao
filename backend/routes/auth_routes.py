from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date, datetime, timedelta, timezone
import httpx
from jose import jwt

from config import ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from models import Usuario
from schemas import LoginSchema, UsuarioSchema, PerfilSchema, LoginResponseSchema, PerfilAtualizarSchema
from dependencies import pegar_sessao, pegar_usuario_logado, calcular_idade, calcular_media_matematica 

auth_routes = APIRouter(prefix="/auth", tags=["Autenticação"])

def criar_token(user_id, duracao_token=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    data_expiracao = datetime.now(timezone.utc) + duracao_token
    dic_info = {"sub": str(user_id), "exp": data_expiracao}
    jwt_codificado = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    return jwt_codificado

URL_TOKEN = "https://suap.ifrn.edu.br/api/token/pair"
URL_MEUS_DADOS = "https://suap.ifrn.edu.br/api/ensino/meus-dados-aluno/"
URL_RH_EU = "https://suap.ifrn.edu.br/api/rh/eu/"
HEADERS_PADRAO = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

@auth_routes.post("/login", response_model=LoginResponseSchema)
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
                user_ano_letivo=int(dados_suap.get('periodo_referencia')) if dados_suap.get('periodo_referencia') else None,
                user_curso=dados_suap.get("curso", ""),
                user_data_nascimento=date.fromisoformat(data_nascimento) if data_nascimento else None,
                user_foto_url=dados_perfil.get("foto", ""),
                user_progresso={},
                user_notas_matematica={},
            )
            
            db.add(usuario)
            db.commit()
            db.refresh(usuario)

        access_token = criar_token(usuario.user_id)
        refresh_token = criar_token(usuario.user_id, duracao_token=timedelta(days=7))

        # Retorna o usuário (o FastAPI usará o UsuarioSchema para formatar a saída automaticamente)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "usuario": usuario,
        }

@auth_routes.get("/perfil", response_model=PerfilSchema, status_code=status.HTTP_200_OK)
async def dados_perfil(usuario: Usuario = Depends(pegar_usuario_logado)):
    """Retorna os dados do perfil do usuário autenticado."""
    return {
        "user_id": usuario.user_id,
        "user_nome": usuario.user_nome,
        "user_matricula": usuario.user_matricula,
        "user_email": usuario.user_email,
        "user_ano_letivo": usuario.user_ano_letivo,
        "user_curso": usuario.user_curso,
        "user_data_nascimento": usuario.user_data_nascimento,
        "user_foto_url": usuario.user_foto_url,
        "user_idade": calcular_idade(usuario.user_data_nascimento),
        "user_media_matematica": calcular_media_matematica(usuario),
    }

@auth_routes.patch("/perfil", response_model=PerfilSchema, status_code=status.HTTP_200_OK)
async def atualizar_perfil(
    dados: PerfilAtualizarSchema,
    usuario: Usuario = Depends(pegar_usuario_logado),
    db: Session = Depends(pegar_sessao),
):
    """Atualiza dados do perfil do usuário autenticado."""
    if dados.user_nome is not None:
        usuario.user_nome = dados.user_nome
    if dados.user_curso is not None:
        usuario.user_curso = dados.user_curso
    if dados.user_foto_url is not None:
        usuario.user_foto_url = dados.user_foto_url
    if dados.user_ano_letivo is not None:
        try:
            usuario.user_ano_letivo = int(dados.user_ano_letivo)
        except (ValueError, TypeError):
            pass

    db.commit()
    db.refresh(usuario)

    return {
        "user_id": usuario.user_id,
        "user_nome": usuario.user_nome,
        "user_matricula": usuario.user_matricula,
        "user_email": usuario.user_email,
        "user_ano_letivo": usuario.user_ano_letivo,
        "user_curso": usuario.user_curso,
        "user_data_nascimento": usuario.user_data_nascimento,
        "user_foto_url": usuario.user_foto_url,
        "user_idade": calcular_idade(usuario.user_data_nascimento),
        "user_media_matematica": calcular_media_matematica(usuario),
    }
