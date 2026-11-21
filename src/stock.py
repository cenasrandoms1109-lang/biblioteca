
from collections import defaultdict


def stock_por_genero(catalogo: dict) -> dict[str, int]:
    """Devolve {género: total de exemplares}."""
    totais = defaultdict(int)
    for livro in catalogo.values():
        for genero in livro.generos:
            totais[genero.strip().title()] += livro.quantidade
    return dict(sorted(totais.items()))


def stock_de_genero(catalogo: dict, genero: str) -> int:
    """Stock total de um género específico (0 se não existir)."""
    return stock_por_genero(catalogo).get(genero.strip().title(), 0)
def take_books_by_gender(books, isbn: str):
    """US9: devolve a lista de géneros do livro com esse ISBN.

    Devolve None se o livro não existir.
    """
    for book in books:
        if book.isbn == isbn:
            return list(book.gender)
    return None
