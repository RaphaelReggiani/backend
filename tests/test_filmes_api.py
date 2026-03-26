from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_criar_filme():
    payload = {
        "titulo": "Matrix",
        "diretor": "Lana Wachowski",
        "ano_lancamento": 1999,
        "genero": "Ficção científica",
    }

    response = client.post("/filmes", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["titulo"] == payload["titulo"]
    assert data["diretor"] == payload["diretor"]
    assert data["ano_lancamento"] == payload["ano_lancamento"]
    assert data["genero"] == payload["genero"]
    assert "id" in data


def test_listar_filmes():
    response = client.get("/filmes")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_buscar_filme_por_id():
    payload = {
        "titulo": "Interestelar",
        "diretor": "Christopher Nolan",
        "ano_lancamento": 2014,
        "genero": "Ficção científica",
    }

    criar = client.post("/filmes", json=payload)
    filme_id = criar.json()["id"]

    response = client.get(f"/filmes/{filme_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == filme_id


def test_buscar_filme_inexistente():
    response = client.get("/filmes/9999")

    assert response.status_code == 404


def test_atualizar_filme():
    payload = {
        "titulo": "Avatar",
        "diretor": "James Cameron",
        "ano_lancamento": 2009,
        "genero": "Ficção científica",
    }

    criar = client.post("/filmes", json=payload)
    filme_id = criar.json()["id"]

    update_payload = {
        "genero": "Aventura"
    }

    response = client.put(f"/filmes/{filme_id}", json=update_payload)

    assert response.status_code == 200
    assert response.json()["genero"] == "Aventura"


def test_deletar_filme():
    payload = {
        "titulo": "Gladiador",
        "diretor": "Ridley Scott",
        "ano_lancamento": 2000,
        "genero": "Drama",
    }

    criar = client.post("/filmes", json=payload)
    filme_id = criar.json()["id"]

    response = client.delete(f"/filmes/{filme_id}")

    assert response.status_code == 204

    buscar = client.get(f"/filmes/{filme_id}")
    assert buscar.status_code == 404