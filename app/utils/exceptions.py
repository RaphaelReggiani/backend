class FilmeNaoEncontradoError(Exception):
    def __init__(self, filme_id: int):
        self.filme_id = filme_id
        super().__init__(f"Filme com id {filme_id} não encontrado.")