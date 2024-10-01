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
