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