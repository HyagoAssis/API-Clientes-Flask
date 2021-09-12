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
  - URL: host/client/update/id

### DELETE
  - Deleta um cliente
  - URL: host/client/delete/id

## Utilização

Utilização e instalação dos requisitos para funcionamento da api de forma local.

  - Primeiro copie o arquivo config_example.py e altera o nome para config.py e coloque as informações do banco de dados referentes.
  
  - Caso não tenha instalado, instale o pacote libpq-dev utilizado o gerenciador de seu sistema operacional, exemplo em ubuntu:
```sh
  sudo apt-get install libpq-dev 
```

  - Em seguida rode o seguinte comando para instalar as dependências na pasta do projeto.  
```sh
  pip install -r requirements.txt
```
  - Após isso rode o comando para rodar o upgrade da migrations e inserir as tabelas no banco de dados
```sh
  python3 -B -m flask db upgrade
```
  - Caso queira excluir as tabelas rode o comando
```sh
  python3 -B -m flask db downgrade
```
  - Por fim, através do comando baixo, rode o servidor local para uso da api.
```sh
  python3 -B -m flask run
```



