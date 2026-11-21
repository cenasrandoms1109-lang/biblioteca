"""Menu principal da aplicação de gestão de biblioteca."""


from src.catalogo import menu_registar, menu_editar, menu_remover
from src.pesquisa import pesquisar_por_isbn
from src.stock import stock_por_genero


def menu_pesquisar_titulo(catalogo):
    """Pede um título e mostra os livros encontrados."""
    titulo = input("Título: ")
    resultados = pesquisar_por_titulo(catalogo, titulo)
    if not resultados:
        print("Nenhum livro encontrado.")
    for livro in resultados:
        print(f"{livro['titulo']} - {livro['autor']}")

def menu_pesquisar_autor(catalogo):
    """Pede um autor e mostra os livros encontrados."""
    autor = input("Autor: ")
    resultados = pesquisar_por_autor(catalogo, autor)
    if not resultados:
        print("Nenhum livro encontrado.")
    for livro in resultados:
        print(f"{livro['titulo']} - {livro['autor']}")

def menu_pesquisar_isbn(catalogo):
    isbn = input("ISBN: ")
    livro = pesquisar_por_isbn(catalogo, isbn)
    if livro:
        print(f"{livro.titulo} - {livro.autor} | Stock: {livro.quantidade}")
    else:
        print("Livro não encontrado.")

def menu_stock_por_genero(catalogo):
    totais = stock_por_genero(catalogo)
    if not totais:
        print("Sem livros no catálogo.")
    for genero, total in totais.items():
        print(f"{genero}: {total}")