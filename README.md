# Livraria - Arquitetura MVC (Lab 7.2)

Aplicação web desenvolvida em Python com Flask para o gerenciamento de um catálogo de livros, aplicando o padrão arquitetural **MVC (Model-View-Controller)**.

## 🏛️ Estrutura do Projeto
O projeto está dividido nas seguintes camadas do MVC:
- **Model (`livraria.py`):** Contém a lógica de dados, as classes e as regras de manipulação do catálogo de livros.
- **View (`templates/index.html`):** Interface web em HTML5/CSS3 estilizada com Jinja2 para exibição dinâmica dos dados e filtros.
- **Controller (`app.py`):** Gerencia as rotas do Flask, intercepta as requisições do usuário, aciona o Model e renderiza a View.

## 🚀 Funcionalidades
- Listagem completa do catálogo de livros.
- Filtro interativo de livros por gênero.
- Interface web responsiva e limpa.

## 🛠️ Como Executar
1. Clone o repositório e acesse a pasta do projeto.
2. Crie e ative um ambiente virtual (`.venv`):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
