from livro import Livro

catalogo = []


def adicionar_livro(livro):
    catalogo.append(livro)


def remover_livro(isbn):
    for livro in catalogo:
        if livro.isbn == isbn:
            catalogo.remove(livro)
            return True

    return False