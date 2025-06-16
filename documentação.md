# Documentação Técnica - Sistema de Denúncias

## 1. Visão Geral

O Sistema de Denúncias é uma aplicação web desenvolvida em Django, projetada para permitir que usuários registrem e gerenciem denúncias, além de fornecer funcionalidades de autenticação. Ele inclui modelos para denúncias e empresas, serializadores para API REST, e templates para a interface do usuário.

## 2. Estrutura do Projeto

A estrutura do projeto segue a convenção de aplicações Django, com módulos bem definidos para cada parte da aplicação:

```
Sistema-Denuncias/
├── __init__.py
├── admin.py                    # Configurações do painel administrativo do Django
├── apps.py                     # Configurações da aplicação Django
├── forms.py                    # Definições de formulários
├── models/                     # Definições dos modelos de dados
│   ├── denuncia.py             # Modelo para Denúncia
│   └── empresa.py              # Modelo para Empresa
├── models.py                   # Modelos de dados (pode conter modelos adicionais ou ser um arquivo de conveniência)
├── migrations/                 # Migrações do banco de dados
│   ├── 0001_initial.py
│   └── __init__.py
├── serializers.py              # Serializadores para API REST (Django REST Framework)
├── templates/                  # Modelos HTML para renderização das páginas
│   ├── auth/                   # Templates relacionados à autenticação
│   │   └── login.html
│   └── denuncias/              # Templates relacionados às denúncias
│       ├── base.html
│       ├── index.html
│       ├── lista_denuncias.html
│       └── nova_denuncia.html
├── tests.py                    # Arquivo para testes da aplicação
├── urls.py                     # Definições de URLs e roteamento
└── views.py                    # Lógica de negócio e views da aplicação
```

## 3. Tecnologias Utilizadas

*   **Django**: Framework web de alto nível para Python.
*   **Django REST Framework (DRF)** (provável, dado `serializers.py`): Para construção de APIs web.
*   **Python**: Linguagem de programação principal.
*   **HTML/CSS**: Para a interface do usuário (através dos templates).
*   **SQLite** (provável, padrão do Django para desenvolvimento): Banco de dados.

## 4. Funcionalidades Principais

O Sistema de Denúncias oferece as seguintes funcionalidades:

*   **Autenticação de Usuários**: Login e gerenciamento de sessões.
*   **Registro de Denúncias**: Permite que usuários criem novas denúncias.
*   **Listagem de Denúncias**: Exibe uma lista de denúncias registradas.
*   **Gerenciamento de Empresas**: Modelos para associar denúncias a empresas.
*   **API RESTful**: (Se `serializers.py` for para DRF) Possibilidade de interação programática com o sistema.
*   **Interface Web**: Páginas para interação do usuário.

## 5. Modelos de Dados

### Denuncia

*   `denuncia.py` (ou definido em `models.py`): Representa uma denúncia, incluindo campos como descrição, status, data, e possivelmente um link para a empresa relacionada.

### Empresa

*   `empresa.py` (ou definido em `models.py`): Representa uma empresa, com campos como nome, CNPJ, etc.

## 6. Configuração e Execução (Ambiente de Desenvolvimento)

Para configurar e executar o projeto em seu ambiente de desenvolvimento, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

*   Python 3.x
*   pip (gerenciador de pacotes do Python)

### Instalação

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
3.  Instale as dependências do projeto (assumindo que há um `requirements.txt` ou que Django e DRF serão instalados manualmente):
    ```bash
    pip install Django djangorestframework  # Adicione djangorestframework se for usado
    # ou pip install -r requirements.txt (se existir)
    ```
4.  Execute as migrações do banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  Crie um superusuário para acessar o painel administrativo (opcional):
    ```bash
    python manage.py createsuperuser
    ```

### Execução

1.  Inicie o servidor de desenvolvimento Django:
    ```bash
    python manage.py runserver
    ```
2.  Acesse o aplicativo no seu navegador em `http://127.0.0.1:8000/` (ou a porta indicada). Os endpoints e páginas específicas dependerão das configurações em `urls.py` e `views.py`.

## 7. Considerações de Desenvolvimento

*   O projeto utiliza o padrão MVT (Model-View-Template) do Django para organização do código.
*   A separação de modelos, views, URLs e templates facilita a manutenção e escalabilidade.
*   A presença de `serializers.py` sugere a capacidade de expor dados via API REST, o que é útil para integração com outras plataformas ou front-ends desacoplados.


