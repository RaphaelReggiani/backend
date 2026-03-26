from sqlalchemy.orm import Session

from app.filmes.models import Filme
from app.filmes.repository import (
    atualizar_filme,
    buscar_filme_por_id,
    criar_filme,
    deletar_filme,
    listar_filmes,
)
from app.filmes.schemas import FilmeAtualizacao, FilmeCriacao
from app.utils.exceptions import FilmeNaoEncontradoError


def criar_filme_service(db: Session, filme_dados: FilmeCriacao) -> Filme:
    return criar_filme(db, filme_dados)


def listar_filmes_service(db: Session) -> list[Filme]:
    return listar_filmes(db)


def buscar_filme_por_id_service(db: Session, filme_id: int) -> Filme:
    filme = buscar_filme_por_id(db, filme_id)

    if filme is None:
        raise FilmeNaoEncontradoError(filme_id)

    return filme


def atualizar_filme_service(
    db: Session,
    filme_id: int,
    filme_dados: FilmeAtualizacao,
) -> Filme:
    filme = buscar_filme_por_id(db, filme_id)

    if filme is None:
        raise FilmeNaoEncontradoError(filme_id)

    return atualizar_filme(db, filme, filme_dados)


def deletar_filme_service(db: Session, filme_id: int) -> None:
    filme = buscar_filme_por_id(db, filme_id)

    if filme is None:
        raise FilmeNaoEncontradoError(filme_id)

    deletar_filme(db, filme)