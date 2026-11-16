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
    livros.append(livro)