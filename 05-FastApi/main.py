from fastapi import FastAPI
from pydantic import BaseModel

class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False

app = FastAPI()

produtos = [
    Produto(id=1, nome="Playstation 5", preco=5000.00, em_oferta=True),
    Produto(id=2, nome="Nintendo Wii", preco=2654.12),
    Produto(id=3, nome="Xbox 360", preco=1765.34, em_oferta=True),
    Produto(id=4, nome="Super Nintendo", preco=234.67),
    Produto(id=5, nome="Atari 2600", preco=199.90, em_oferta=True)
]

@app.get("/")
async def index():
    return {"Hello": "World"}

@app.get('/produtos/{id}')
async def produto(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return {"error": "Produto não encontrado"}

@app.put('/produtos/{id}')
async def atualiza_produto(id: int, produto: Produto):
    for produto_atual in produtos:
        if produto_atual.id == id:
            produto_atual = produto
            return produto_atual
    
    return {"error": "Produto não encontrado"}