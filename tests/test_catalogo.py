"""
Testes das operações do catálogo de livros.

:Date: 16 Novembro 2026
:Authors: João Pedro Balbino, Gonçalo Losada
"""

import unittest
from src.catalogo import registar_livro, editar_livro, remover_livro


class TestRegistarLivro(unittest.TestCase):
    """Testes da função registar_livro"""

    def test_registar_livro_valido(self):
        livros = []
        registar_livro(livros, {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "isbn": "9780306406157"})
        self.assertEqual(len(livros), 1)

    def test_titulo_vazio(self):
        livros = []
        with self.assertRaises(ValueError): registar_livro(livros, {"titulo": "", "autor": "Machado de Assis", "isbn": "9780306406157"})
        
    def test_isbn_duplicado(self):
        livros = []
        registar_livro(livros, {"titulo": "A", "autor": "B", "isbn": "9780306406157"})
        with self.assertRaises(ValueError):
            registar_livro(livros, {"titulo": "C", "autor": "D", "isbn": "9780306406157"})
    




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

    def test_titulo_vazio(self):
        livros = self.criar_livros()
        with self.assertRaises(ValueError):
            editar_livro(livros, "9780306406157", {"titulo": ""})

class TestRemoverLivro(unittest.TestCase):
    def test_remover_existente(self):
        livros = [{"titulo": "A", "autor": "B", "isbn": "9780306406157"}]
        self.assertTrue(remover_livro(livros, "9780306406157"))
        self.assertEqual(len(livros), 0)

    def test_remover_inexistente(self):
        self.assertFalse(remover_livro([], "9780306406157"))
    
    def test_remover_com_hifens(self):
        livros = [{"titulo": "A", "autor": "B", "isbn": "9780306406157"}]
        self.assertTrue(remover_livro(livros, "978-0-306-40615-7"))
        self.assertEqual(len(livros), 0)