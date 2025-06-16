# Sistema de Denúncias

Um sistema web para registro e gerenciamento de denúncias, desenvolvido com Django, oferecendo funcionalidades de autenticação e gestão de informações de denúncias e empresas.

## ✨ Funcionalidades

*   **Autenticação de Usuários**: Login e controle de acesso.
*   **Registro de Denúncias**: Crie e gerencie denúncias.
*   **Listagem de Denúncias**: Visualize todas as denúncias registradas.
*   **Gerenciamento de Empresas**: Associe denúncias a empresas.

## 🚀 Tecnologias Utilizadas

*   **Django**: Framework web Python.
*   **Django REST Framework** (provável): Para construção de APIs.
*   **Python**: Linguagem de programação.
*   **HTML/CSS**: Para a interface do usuário.
*   **SQLite**: Banco de dados (padrão para desenvolvimento).

## ⚙️ Instalação e Execução

Para rodar este projeto em seu ambiente local, siga os passos abaixo:

### Pré-requisitos

*   Python 3.x
*   pip

### Passos

1.  Clone o repositório:
    ```bash
    git clone https://github.com/rafaelcrb/Sistema-Denuncias.git
    cd Sistema-Denuncias
    ```
2.  Crie e ative um ambiente virtual (recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # venv\Scripts\activate   # No Windows
    ```
3.  Instale as dependências:
    ```bash
    pip install Django djangorestframework  # Adicione djangorestframework se for usado
    ```
4.  Execute as migrações do banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  (Opcional) Crie um superusuário para o painel administrativo:
    ```bash
    python manage.py createsuperuser
    ```
6.  Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
    Acesse o aplicativo em `http://127.0.0.1:8000/` (ou a porta indicada).

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


