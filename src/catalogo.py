"""
Operações sobre o catálogo de livros (registar, editar e remover)

:Date: 16 Novembro 2026
:Version: 1.0
:Authors: João Pedro Balbino
"""


def registar_livro(livros, livro):
    """
    Regista um novo livro no catálogo

    :param livros: lista com todos os livros já registados
    :type livros: list
    :param livro: dicionário com os dados do livro a registar
    :type livro: dict
    :return: nada, o livro é acrescentado à lista recebida
    :rtype: None
    """

    if not livro["titulo"]:
        raise ValueError("O título é obrigatório.")
    if not livro["autor"]:
        raise ValueError("O autor é obrigatório.")
    
    isbn = livro["isbn"].replace("-", "").replace(" ", "")
    if not (isbn.isdigit() and len(isbn) in (10, 13)):
        raise ValueError("O ISBN deve ter 10 ou 13 dígitos.")
    livros.append(livro)


def editar_livro(livros, isbn, novos_dados):
    """
    Edita os dados de um livro já registado no sistema

    :param livros: lista com todos os livros registados
    :type livros: list
    :param isbn: ISBN do livro
    :type isbn: str
    :param novos_dados: campos a alterar 
    :type novos_dados: dict
    :raises ValueError: se o livro não existir
    """
    if "titulo" in novos_dados and not novos_dados["titulo"]:
        raise ValueError("O titulo é obrigatório!")
    if "autor" in novos_dados and not novos_dados["autor"]:
        raise ValueError("O autor é obrigatório!")

    isbn = isbn.replace("-", "").replace(" ", "")

    for livro in livros:
        isbn_livro = livro["isbn"].replace("-", "").replace(" ", "")
        if isbn_livro == isbn:
            for campo in novos_dados:
                if campo != "isbn":
                    livro[campo] = novos_dados[campo]
            return

    raise ValueError("Livro não foi encontrado!")


def menu_registar(livros):
    """Pede os dados ao utilizador e regista um livro

    :param livros: lista de livros do catálogo
    :type livros: list
    """
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")

    try:
        registar_livro(livros, {"titulo": titulo, "autor": autor, "isbn": isbn})
        print("Livro registado!")
    except ValueError as erro:
        print(f"Erro: {erro}")
  