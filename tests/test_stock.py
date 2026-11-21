import unittest

from src.stock import take_books_by_gender

LIVROS = [
    {
        "isbn": "222",
        "titulo": "Memorial do Convento",
        "autor": "José Saramago",
        "generos": ["Romance", "Histórico"],
        "quantidade": 2,
    }
]


class TestGeneros(unittest.TestCase):
    def test_generos_do_livro(self):
        self.assertEqual(take_books_by_gender(LIVROS, "222"), ["Romance", "Histórico"])

    def test_livro_inexistente(self):
        self.assertIsNone(take_books_by_gender(LIVROS, "999"))


if __name__ == "__main__":
    unittest.main()