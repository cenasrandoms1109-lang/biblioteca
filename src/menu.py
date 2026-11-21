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

def menu_generos_livro(catalogo):
    """Pede um ISBN e mostra os géneros desse livro."""
    isbn = input("ISBN do livro: ")
    try:
        generos = generos_do_livro(catalogo, isbn)
        print("Géneros: " + ", ".join(generos))
    except ValueError as erro:
        print(f"Erro: {erro}")
        
def mostrar_menu():
    """Mostra as opções do menu."""
    print("\n=== Biblioteca ===")
    print("1. Registar livro")
    print("2. Editar livro")
    print("3. Remover livro")
    print("4. Pesquisar por título")
    print("5. Pesquisar por autor")
    print("6. Pesquisar por ISBN")
    print("7. Stock por género")
    print("8. Géneros de um livro")
    print("0. Sair")