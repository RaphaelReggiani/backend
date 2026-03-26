from fastapi import FastAPI

from app.core.database import Base, engine
from app.filmes.router import router as filmes_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Filmes - Wattio",
    description="API REST para gerenciamento de filmes.",
    version="1.0.0",
)

app.include_router(filmes_router)


@app.get("/")
def root():
    return {"mensagem": "API de filmes em execução."}