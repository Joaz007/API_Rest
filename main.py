from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="API Loja Gamer",
    description="API REST didática para gerenciar jogos, consoles e acessórios.",
    version="1.0.0",
)


class DadosProduto(BaseModel):
    nome: str = Field(min_length=2, examples=["PlayStation 5 Slim"])
    categoria: str = Field(min_length=2, examples=["Console"])
    preco: float = Field(gt=0, examples=[3499.90])
    estoque: int = Field(ge=0, examples=[8])


class Produto(DadosProduto):
    id: int = Field(gt=0, examples=[1])


# Dados ilustrativos em memória; não representam preços reais de mercado.
produtos = [
    Produto(id=1, nome="PlayStation 5 Slim", categoria="Console", preco=3499.90, estoque=5),
    Produto(id=2, nome="Nintendo Switch OLED", categoria="Console", preco=2199.90, estoque=7),
    Produto(id=3, nome="Controle sem fio", categoria="Acessório", preco=299.90, estoque=12),
    Produto(id=4, nome="Jogo de aventura", categoria="Jogo", preco=249.90, estoque=9),
]


@app.get("/")
def inicio():
    return {
        "mensagem": "API Loja Gamer funcionando!",
        "documentacao": "/docs",
        "produtos": "/produtos/",
    }


@app.get("/produtos/", response_model=list[Produto])
def listar_produtos():
    return produtos


@app.get("/produtos/{produto_id}/", response_model=Produto)
def consultar_produto(produto_id: int):
    for produto in produtos:
        if produto.id == produto_id:
            return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")


@app.post("/produtos/", response_model=Produto, status_code=status.HTTP_201_CREATED)
def cadastrar_produto(produto: Produto):
    for existente in produtos:
        if existente.id == produto.id:
            raise HTTPException(status_code=409, detail="Já existe um produto com esse ID")
    produtos.append(produto)
    return produto


@app.put("/produtos/{produto_id}/", response_model=Produto)
def atualizar_produto(produto_id: int, novos_dados: DadosProduto):
    for indice, produto in enumerate(produtos):
        if produto.id == produto_id:
            atualizado = Produto(id=produto_id, **novos_dados.model_dump())
            produtos[indice] = atualizado
            return atualizado
    raise HTTPException(status_code=404, detail="Produto não encontrado")


@app.delete("/produtos/{produto_id}/")
def excluir_produto(produto_id: int):
    for indice, produto in enumerate(produtos):
        if produto.id == produto_id:
            del produtos[indice]
            return {"mensagem": "Produto excluído com sucesso", "id": produto_id}
    raise HTTPException(status_code=404, detail="Produto não encontrado")
