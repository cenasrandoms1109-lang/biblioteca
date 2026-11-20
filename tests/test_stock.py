import unittest

from src.livro import Livro
from src.stock import take_books_by_gender

LIVROS = [Livro("222", "Memorial do Convento", "José Saramago", ["Romance", "Histórico"], 2)]


class TestGeneros(unittest.TestCase):
    def test_generos_do_livro(self):
        self.assertEqual(take_books_by_gender(LIVROS, "222"), ["Romance", "Histórico"])

    def test_livro_inexistente(self):
        self.assertIsNone(take_books_by_gender(LIVROS, "999"))


if __name__ == "__main__":
    unittest.main()
