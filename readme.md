# Projeto Flask de Gestão de Produção e Despejo
=============================================

Este projeto é uma aplicação web desenvolvida em Flask para a gestão de dados de produção de plástico global e participação no despejo de resíduos no oceano. Ele permite realizar operações CRUD (Create, Read, Update, Delete) nos registros de produção e despejo, bem como exportar os dados em formato JSON e aplicar filtros de busca.

Funcionalidades
---------------

-   **Produção de Plástico**

    -   Inserção de novos registros de produção.
    -   Listagem de registros existentes.
    -   Edição e exclusão de registros.
    -   Filtro de busca por entidade, ano e produção anual.
-   **Participação no Despejo**

    -   Inserção de novos registros de despejo.
    -   Listagem de registros existentes.
    -   Edição e exclusão de registros.
    -   Filtro de busca por entidade, código, ano e participação.
-   **Exportação de Dados**

    -   Exportação de registros de produção ou despejo em formato JSON.



Configuração do Ambiente
------------------------

1.  **Clone o repositório**

    sh

    Copiar código

    `git clone <https://github.com/rafaelnxd/GSCrud>
    cd <GSCrud>`

2.  **Crie um ambiente virtual e ative-o**

    sh

    Copiar código

    `python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate``

3.  **Instale as dependências**

    sh

    Copiar código

    `pip install -r requirements.txt`

4.  **Configuração do Banco de Dados**

    -   Crie um banco de dados e atualize a string de conexão `SQL_KEY` no arquivo `models/connection.py`.
    -   Atualize a chave secreta `SECRET_KEY` no arquivo `models/connection.py`.
5.  **Inicialize o Banco de Dados**

    -   Execute o script de insert.py para fazer a criação das tabelas e inserir os dados dos CSV nelas.


Execução
--------

1.  **Execute a aplicação**

    sh

    Copiar código

    `python app.py`

2.  **Acesse no navegador**

    arduino

    Copiar código

    `http://127.0.0.1:5000`


Rotas
-----

-   **Produção**

    -   `GET /producao`: Lista todos os registros de produção.
    -   `POST /producao`: Insere um novo registro de produção.
    -   `DELETE /excluir/<int:id>`: Exclui um registro de produção.
    -   `GET /editar/<int:id>`: Obtém os dados de um registro de produção específico.
    -   `POST /editar`: Edita um registro de produção existente.
    -   `POST /search_filter_producao`: Filtra os registros de produção com base em um termo de busca.
-   **Despejo**

    -   `GET /despejo`: Lista todos os registros de despejo.
    -   `POST /despejo`: Insere um novo registro de despejo.
    -   `DELETE /excluirDes/<int:id>`: Exclui um registro de despejo.
    -   `GET /editarDes/<int:id>`: Obtém os dados de um registro de despejo específico.
    -   `POST /editarDes`: Edita um registro de despejo existente.
    -   `POST /search_filter_despejo`: Filtra os registros de despejo com base em um termo de busca.
-   **Exportação**

    -   `POST /export_json`: Exporta os dados de produção ou despejo em formato JSON.
-   **Página Inicial**

    -   `GET /`: Página inicial da aplicação.

