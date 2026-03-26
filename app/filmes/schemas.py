from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class FilmeBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=255)
    diretor: str = Field(..., min_length=1, max_length=255)
    ano_lancamento: int = Field(..., ge=1888, le=2100)
    genero: str = Field(..., min_length=1, max_length=100)


class FilmeCriacao(FilmeBase):
    pass


class FilmeAtualizacao(BaseModel):
    titulo: str | None = Field(None, min_length=1, max_length=255)
    diretor: str | None = Field(None, min_length=1, max_length=255)
    ano_lancamento: int | None = Field(None, ge=1888, le=2100)
    genero: str | None = Field(None, min_length=1, max_length=100)


class FilmeResposta(FilmeBase):
    id: int
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)