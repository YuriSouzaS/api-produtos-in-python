# API de produtos
Este projeto expõe uma API RESTful para gerenciar informações de produtos.

### Endpoints Disponíveis:

* GET /produtos:
  * Descrição: Retorna uma lista de todos os produtos cadastrados.
  * Resposta: Um array de objetos, onde cada objeto representa um produto.
  * Campos:
    * id: Identificador único do produto (string).
    * name: Nome do produto (string).
    * amount: Quantidade disponível do produto (número).
    * desc: Descrição do produto (string).
    * image: URL da imagem do produto (string).
    * price: Preço do produto (número).

* GET /produtos/exists/id
  * Descrição: Retona uma mensagem, case o produto exista no banco de dados
  * Resposta: True caso exista, False caso contrário

* GET /produtos/id
  * Descrição: Retorna todas as informações de um produto
  * Campos: 
    * id: Identificador único do produto (string).
    * name: Nome do produto (string).
    * amount: Quantidade disponível do produto (número).
    * desc: Descrição do produto (string).
    * image: URL da imagem do produto (string).
    * price: Preço do produto (número).

* POST /produtos/add/
  * Descrição: Criar um novo produto
  * Resposta: Mensagem "Success, caso de tudo ocorra bem
  * Campos:
    * name: Nome do produto (string).
    * amount: Quantidade disponível do produto (número).
    * desc: Descrição do produto (string).
    * image: URL da imagem do produto (string).
    * price: Preço do produto (número).

* PUT /produtos/alter/id
  * Descrição: Altera somente o campo amount
  * Resposta: mensagem "Success", caso de tudo ocorra bem
  * Campos:
    * amount: Quantidade disponível do produto (número).

* DELETE /produtos/delete/id
  * Descrição: Deleta o produto com o id passado
  * Resposta: mensagem "Success", caso de tudo ocorra bem
  * Campos:
    * name: Nome do produto (string).
    * amount: Quantidade disponível do produto (número).
    * desc: Descrição do produto (string).
    * image: URL da imagem do produto (string).
    * price: Preço do produto (número).
  
