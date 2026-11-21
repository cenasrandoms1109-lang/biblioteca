from collections import defaultdict

from src.catalogo import limpar_isbn


def stock_por_genero(livros):
    """Devolve {género: total de exemplares}."""
    totais = defaultdict(int)
    for livro in livros:
        for genero in livro.get("generos", []):
            totais[genero.strip().title()] += livro.get("quantidade", 0)
    return dict(sorted(totais.items()))


def stock_de_genero(livros, genero):
    """Stock total de um género específico (0 se não existir)."""
    return stock_por_genero(livros).get(genero.strip().title(), 0)


def take_books_by_gender(livros, isbn):
    """Devolve a lista de géneros do livro com esse ISBN (None se não existir)."""
    isbn = limpar_isbn(isbn)
    for livro in livros:
        if limpar_isbn(livro["isbn"]) == isbn:
            return list(livro.get("generos", []))
    return None