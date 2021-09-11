# Prova Python

Projeto desenvolvido como prova no processo seletivo para Desenvolvedor Python na Smart NX.

O Projeto trata-se de criar um API REST com um CRUD Clients.

Tecnologias Utilizadas:
 - Python 3.8.10
 - PostgreSQL
 - Flask
 - SQL Alchemy

## Autor
Hyago Assis de Novais Oliveira

## Métodos

### GET
  - Retorna a lista de clientes
  - URL: host/clients

### POST
  - Criar um cliente
  - URL: host/client/create

### PUT
  - Edita as informações de um cliente
  - URL: host/client/edit/id

### DELETE
  - Deleta um cliente
  - URL: host/client/delete/id

## Utilização

Utilização e instalação dos requisitos para funcionamento da api de forma local.

  - Primeiro copie o arquivo config_example.py e altera o nome para config.py e coloque as informações do banco de dados referentes.

  - Em seguida rode o seguinte comando para instalar as dependências na pasta do projeto.  
```sh
  pip install -r requirements.txt
```
  - Após isso rode o comando para rodar os upgrade da migrations e inserir as tabelas no banco de dados
```sh
  flask db upgrade
```
  - Caso queira excluir as tabelas rode o comando
```sh
  flask db downgrade
```
  - Por fim, através do comando baixo, rode o servidor local para uso da api.
```sh
  flask run
```



