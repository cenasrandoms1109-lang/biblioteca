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