"""
Testes das operações do catálogo de livros.

:Date: 16 Novembro 2026
:Authors: João Pedro Balbino
"""

import unittest
from src.catalogo import registar_livro
from src.catalogo import registar_livro, editar_livro


class TestRegistarLivro(unittest.TestCase):
    """Testes da função registar_livro"""

    def test_registar_livro_valido(self):
        livros = []
        registar_livro(livros, {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "isbn": "9780306406157"})
        self.assertEqual(len(livros), 1)

    def test_titulo_vazio(self):
        livros = []
        with self.assertRaises(ValueError): registar_livro(livros, {"titulo": "", "autor": "Machado de Assis", "isbn": "9780306406157"})




class  TestEditarLivro(unittest.TestCase):
    """Testes da função editar_livro"""

    def criar_livros(self):
        """Cria uma lista com um livro para usar nos testes"""
        return [{"titulo": "Dom Casmurro","autor": "Machado de Assis","isbn": "9780306406157"}]

    def test_editar_com_sucesso(self):
        """Edita o título de um livro existente"""
        livros = self.criar_livros()
        editar_livro(livros, "9780306406157", {"titulo": "Novo Titulo"})
        self.assertEqual(livros[0]["titulo"], "Novo Titulo")

    def test_isbn_inexistente(self):
        """Dá erro quando o ISBN não está na lista"""
        livros = self.criar_livros()
        with self.assertRaises(ValueError):
            editar_livro(livros, "0000000000", {"titulo": "Novo"})

    def test_isbn_nao_muda(self):
        livros = self.criar_livros()
        editar_livro(livros, "9780306406157", {"isbn": "0000000000"})
        self.assertEqual(livros[0]["isbn"], "9780306406157")