# FLASH API Python

Este é o meu primeiro projeto de desenvolvimento de uma **API RESTful** utilizando **Python**. O objetivo principal desse projeto foi praticar e aprender como construir uma API utilizando o **Flask**, **SQLAlchemy** para manipulação de banco de dados e **Flask-RESTful** para criar recursos RESTful de forma simples e eficiente.

## Tecnologias Utilizadas

- **Python 3.x**
- **Flask**: Framework web para construção de APIs.
- **SQLAlchemy**: ORM (Object-Relational Mapper) para interação com o banco de dados.
- **Flask-RESTful**: Extensão para a criação de APIs RESTful de forma simplificada.

## Funcionalidades

- **GET `/users/`**: Retorna uma lista de todos os usuários cadastrados no banco de dados.
- **POST `/users/`**: Cria um novo usuário no banco de dados, recebendo o `name` e `email` como dados.
- **PUT `/user/{id}`**: Atualiza o usuário, recebendo o `name` e `email`.
- **DELETE `/user/{id}`**: Deleta o usuário.

## Como Rodar o Projeto

1. Clone este repositório:
    ```bash
    git clone https://github.com/Gus1331/FLASH-API-PYTHON.git
    cd FLASH-API-PYTHON
    ```

2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:
    - No **Windows**:
      ```bash
      .\venv\Scripts\activate
      ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Crie o banco de dados:
    ```bash
    python create_db.py
    ```

6. Inicie a aplicação Flask:
    ```bash
    python api.py
    ```

7. A API estará rodando em **http://127.0.0.1:5000/**. Você pode acessar a página inicial e testar os endpoints `/users/` com ferramentas como Postman ou diretamente no navegador.

## Como Usar

- **GET `/users/`**: Retorna todos os usuários cadastrados.
- **POST `/users/`**: Envia os dados `name` e `email` no corpo da requisição para criar um novo usuário. Exemplo:
  
  ```json
  {
    "name": "John Doe",
    "email": "johndoe@example.com"
  }
