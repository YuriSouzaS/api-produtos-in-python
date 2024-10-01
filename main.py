from fastapi import FastAPI
from model import select_all, insert, alter, delete

app = FastAPI()

# RETORNA TODOS OS PRODUTOS
@app.get('/')
async def read_produtos():
    produtos = select_all()
    return produtos

# CHECA A EXISTÊNCIA DE UM PRODUTOS PELO ID
@app.get('/produtos/exists/{id}')
async def id_exists(id: str):
    produtos = select_all()
    return id in produtos

# RETORNA UM PRODUTO COM BASE NO SEU ID
@app.get('/produtos/{id}')
async def read_produtos_with_id(id: str):
    produtos = select_all()
    return produtos[id]

# ADICIONAR UM PRODUTO
@app.post('/produtos/add/')
async def add_produtos(name: str, amount: int, desc: str, image: str, price: float):
    insert(name, amount, desc, image, price)
    return "Success!"

# ALTERAR UM PRODUTO
@app.put('/produtos/alter/{id}')
async def alter_produto(amount: int, id: int):
    alter(amount, id )
    return "Success"

# DELETAR UM PRODUTO
@app.delete('/produtos/delete/{id}')
async def delete_produto(id: int):
    delete(id)
    return "Success"