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
import unicodedata


def _normalize(text: str):
    """Minúsculas e sem acentos, para pesquisar 'jose' e encontrar 'José'."""
    no_acentes = unicodedata.normalize("NFD", text)
    no_acentes = "".join(c for c in no_acentes if unicodedata.category(c) != "Mn")
    return no_acentes.lower().strip()


def search_by_title(book, term: str):
    """US5: devolve os livros cujo título contém o termo."""
    term = _normalize(term)
    if not term:
        return []
    return [l for l in book if term in _normalize(l.titulo)]


def search_by_author(book, term: str) -> list:
    """US6: devolve os livros cujo autor contém o termo."""
    term = _normalize(term)
    if not term:
        return []
    return [l for l in book if term in _normalize(l.autor)]
