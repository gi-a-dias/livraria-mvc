# livraria.py (Model)

def obter_livros():
    """Retorna a base de dados simulada dos livros da livraria."""
    return [
        {"id": 1, "titulo": "O Hobbit", "genero": "Fantasia", "preco": 45.0, "estoque": 1},
        {"id": 2, "titulo": "1984", "genero": "Ficção", "preco": 30.0, "estoque": 5},
        {"id": 3, "titulo": "Senhor dos Anéis", "genero": "Fantasia", "preco": 60.0, "estoque": 2}
    ]

def filtrar_por_genero(genero):
    """Regra de negócio para filtrar livros."""
    livros = obter_livros()
    if not genero:
        return livros
    return [l for l in livros if l["genero"].lower() == genero.lower()]