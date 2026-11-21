def normalizar_isbn(isbn: str) -> str:
    """Remove hífenes e espaços: '978-972-0-12345-6' -> '9789720123456'."""
    return isbn.replace("-", "").replace(" ", "").strip().upper()


def pesquisar_por_isbn(catalogo: dict, isbn: str):
    """Devolve o Livro com esse ISBN, ou None se não existir."""
    isbn_norm = normalizar_isbn(isbn)
    for livro in catalogo.values():
        if normalizar_isbn(livro.isbn) == isbn_norm:
            return livro
    return None