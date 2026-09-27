# IFunção — Backend

API REST responsável pela autenticação de usuários, regras de negócio, gerenciamento do banco de dados e integração com o sistema de ensino do IFRN para a plataforma **IFunção**.

---

## Tecnologias Utilizadas

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Linguagem:** [Python](https://www.python.org/)
* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Migrações:** [Alembic](https://alembic.sqlalchemy.org/)
* **Banco de Dados:** SQLite (`banco.db`)
* **Autenticação:** JWT (`python-jose`) e integração HTTP assíncrona (`httpx`) com a API do **SUAP/IFRN**
* **Validação de Dados:** [Pydantic](https://docs.pydantic.dev/)

---

## Estrutura de Arquivos

* `main.py` — Ponto de entrada da aplicação, inclusão de rotas e configurações de CORS.
* `models.py` — Definição das tabelas e relacionamentos do banco de dados (SQLAlchemy).
* `schemas.py` — Modelos Pydantic para validação das requisições e respostas da API.
* `dependencies.py` — Gerenciamento de sessões do banco de dados e middleware de autenticação via token JWT (`pegar_usuario_logado`).
* `routes/auth_routes.py` — Endpoints para login via SUAP e consulta ao perfil do estudante.
* `alembic/` — Scripts e arquivos de migração autogerados (`env.py`).

---

## Entidades do Banco de Dados (`models.py`)

* **`Usuario` (`usuarios`):** Armazena dados cadastrais do estudante sincronizados com o SUAP (nome, matrícula, e-mail acadêmico, curso, foto e dias de ofensiva).
* **`Acesso` (`acessos`):** Registra as sessões de uso dos estudantes (data, hora de início e fim).
* **`Conteudo` (`conteudos`):** Tópicos pedagógicos de matemática (nome, etapa e links de slides/PDFs).
* **`Questao` (`questoes`):** Banco de questões focado no ENEM (enunciado, alternativas em JSON, etapa, nível de dificuldade e gabarito).
* **`Usuario_Conteudo` (`usuario_conteudos`):** Acompanhamento do progresso dos alunos nos tópicos da disciplina.
* **`Resposta_Questao` (`resposta_questoes`):** Histórico de resoluções de questões pelos usuários para fins de estatística e aprendizado.

---

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do diretório `backend/` contendo as seguintes configurações:

```env
SECRET_KEY=sua_chave_secreta_jwt
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## Como Executar

### Pré-requisitos

* **Python** (versão 3.10 ou superior)
* **pip** e **venv**

### Passo a passo

1. Acesse o diretório do backend:
```
cd backend
```


2. Crie e ative o ambiente virtual:
* **Linux / macOS:**
```
python3 -m venv venv
source venv/bin/activate
```


* **Windows:**
```
python -m venv env
.\env\Scripts\activate
```

3. Instale as dependências exigidas pelo projeto:
```
pip install fastapi uvicorn sqlalchemy alembic pydantic python-jose python-dotenv httpx
```

4. Execute as migrações do banco de dados com Alembic:
```
alembic upgrade head
```

5. Inicie o servidor em modo de desenvolvimento:

```
uvicorn main:app --reload
```
6. Acesse a documentação interativa das rotas:
* **Swagger UI:** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)