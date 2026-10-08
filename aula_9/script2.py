from fastapi import FastAPI

app = FastAPI()


@app.get("/livros/{livro_id}")
def obter_livro(livro_id: int):
    # restante
    return