from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.filmes.schemas import FilmeAtualizacao, FilmeCriacao, FilmeResposta
from app.filmes.service import (
    atualizar_filme_service,
    buscar_filme_por_id_service,
    criar_filme_service,
    deletar_filme_service,
    listar_filmes_service,
)
from app.utils.exceptions import FilmeNaoEncontradoError

router = APIRouter(prefix="/filmes", tags=["Filmes"])


@router.post(
    "",
    response_model=FilmeResposta,
    status_code=status.HTTP_201_CREATED,
)
def criar_filme_endpoint(
    filme_dados: FilmeCriacao,
    db: Session = Depends(get_db),
):
    return criar_filme_service(db, filme_dados)


@router.get(
    "",
    response_model=list[FilmeResposta],
    status_code=status.HTTP_200_OK,
)
def listar_filmes_endpoint(db: Session = Depends(get_db)):
    return listar_filmes_service(db)


@router.get(
    "/{filme_id}",
    response_model=FilmeResposta,
    status_code=status.HTTP_200_OK,
)
def buscar_filme_por_id_endpoint(
    filme_id: int,
    db: Session = Depends(get_db),
):
    try:
        return buscar_filme_por_id_service(db, filme_id)
    except FilmeNaoEncontradoError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.put(
    "/{filme_id}",
    response_model=FilmeResposta,
    status_code=status.HTTP_200_OK,
)
def atualizar_filme_endpoint(
    filme_id: int,
    filme_dados: FilmeAtualizacao,
    db: Session = Depends(get_db),
):
    try:
        return atualizar_filme_service(db, filme_id, filme_dados)
    except FilmeNaoEncontradoError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.delete(
    "/{filme_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def deletar_filme_endpoint(
    filme_id: int,
    db: Session = Depends(get_db),
):
    try:
        deletar_filme_service(db, filme_id)
    except FilmeNaoEncontradoError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc