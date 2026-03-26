from sqlalchemy.orm import Session

from app.filmes.models import Filme
from app.filmes.schemas import FilmeAtualizacao, FilmeCriacao


def criar_filme(db: Session, filme_dados: FilmeCriacao) -> Filme:
    filme = Filme(**filme_dados.model_dump())
    db.add(filme)
    db.commit()
    db.refresh(filme)
    return filme


def listar_filmes(db: Session) -> list[Filme]:
    return db.query(Filme).order_by(Filme.id.asc()).all()


def buscar_filme_por_id(db: Session, filme_id: int) -> Filme | None:
    return db.query(Filme).filter(Filme.id == filme_id).first()


def atualizar_filme(
    db: Session,
    filme: Filme,
    filme_dados: FilmeAtualizacao,
) -> Filme:
    dados_atualizacao = filme_dados.model_dump(exclude_unset=True)

    for campo, valor in dados_atualizacao.items():
        setattr(filme, campo, valor)

    db.commit()
    db.refresh(filme)
    return filme


def deletar_filme(db: Session, filme: Filme) -> None:
    db.delete(filme)
    db.commit()