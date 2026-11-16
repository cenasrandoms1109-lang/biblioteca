"""
Testes das operações do catálogo de livros.

:Date: 16 Novembro 2026
:Authors: João Pedro Balbino
"""

import unittest

from src.catalogo import registar_livro


class TestRegistarLivro(unittest.TestCase):
    """Testes da função registar_livro."""

    def test_registar_livro_valido(self):
        livros = []
        registar_livro(livros, {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "isbn": "9780306406157"})
        self.assertEqual(len(livros), 1)

    def test_titulo_vazio(self):
        livros = []
        with self.assertRaises(ValueError): registar_livro(livros, {"titulo": "", "autor": "Machado de Assis", "isbn": "9780306406157"})