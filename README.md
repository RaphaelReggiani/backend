# WATTIO - Backend Challenge

## Descrição do desafio

O desafio consiste em implementar um CRUD de filmes utilizando Python, integrando com uma API REST e uma possível persistência de dados.

### Rotas mínimas esperadas

- `GET /filmes` → retorna todos os filmes cadastrados  
- `POST /filmes` → cadastra um novo filme  
- `GET /filmes/{id}` → retorna um filme específico  

O objetivo do desafio é avaliar a capacidade de desenvolvimento, organização do código e adaptação às tecnologias utilizadas.

---

# Implementação da solução

Esta implementação foi desenvolvida utilizando **FastAPI** com arquitetura modular e separação de responsabilidades.

Além das rotas mínimas solicitadas no desafio, a implementação inclui endpoints adicionais para atualização e remoção de registros, formando um CRUD completo.

---

# Tecnologias utilizadas

- Python 3.13
- FastAPI
- SQLAlchemy
- Pydantic
- Pytest
- SQLite
- Docker / Docker Compose

---

# Arquitetura do projeto

A aplicação segue uma arquitetura organizada em camadas:

```
Router → Service → Repository → Database
```

- **Router** → define os endpoints da API
- **Service** → contém as regras de negócio
- **Repository** → acesso ao banco de dados
- **Database** → configuração da conexão e sessão

Essa separação facilita manutenção, testes e escalabilidade.

---

# Estrutura do projeto

```
backend
│
├── app
│   ├── core
│   │   └── database.py
│   │
│   ├── filmes
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── repository.py
│   │   ├── service.py
│   │   └── router.py
│   │
│   ├── utils
│   │   └── exceptions.py
│   │
│   └── main.py
│
├── tests
│   └── test_filmes_api.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Como executar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/RaphaelReggiani/backend.git
cd backend
```

---

## 2. Criar ambiente virtual

```bash
python -m venv venv
```

Ativar:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 4. Executar a aplicação

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

Documentação automática:

```
http://127.0.0.1:8000/docs
```

---

# Endpoints da API

### Criar filme

```
POST /filmes
```

Exemplo de payload:

```json
{
  "titulo": "Interestelar",
  "diretor": "Christopher Nolan",
  "ano_lancamento": 2014,
  "genero": "Ficção científica"
}
```

---

### Listar filmes

```
GET /filmes
```

---

### Buscar filme por ID

```
GET /filmes/{id}
```

---

### Atualizar filme

```
PUT /filmes/{id}
```

---

### Remover filme

```
DELETE /filmes/{id}
```

---

# Testes automatizados

Os testes foram implementados utilizando **pytest** e **FastAPI TestClient**.

Para executar:

```bash
pytest
```

Os testes cobrem:

- criação de filmes
- listagem
- busca por ID
- atualização
- remoção
- validação de erro (filme inexistente)

---

# Execução com Docker

O projeto inclui configuração para execução em container utilizando Docker e Docker Compose.

### Build e execução

```bash
docker compose up --build
```

Após iniciar:

```
http://localhost:8000/docs
```

---

# Considerações finais

Esta implementação prioriza:

- organização do código
- separação de responsabilidades
- facilidade de manutenção
- testes automatizados
- documentação clara da API

A estrutura permite evolução futura da aplicação sem grandes refatorações.