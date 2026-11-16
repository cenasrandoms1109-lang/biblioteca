import unittest
from src.livro import Livro
from src.pesquisa import pesquisar_por_isbn
from src.stock import stock_por_genero, stock_de_genero


class TestPesquisaIsbn(unittest.TestCase):
    def setUp(self):
        self.cat = {"9789720123456": Livro("9789720123456", "A", "X", ["Romance"], 3)}

    def test_encontra(self):
        self.assertEqual(pesquisar_por_isbn(self.cat, "978-972-0123456").titulo, "A")

    def test_nao_encontra(self):
        self.assertIsNone(pesquisar_por_isbn(self.cat, "000"))


class TestStock(unittest.TestCase):
    def setUp(self):
        self.cat = {
            "1": Livro("1", "A", "X", ["Romance"], 3),
            "2": Livro("2", "B", "Y", ["Romance", "Drama"], 2),
        }

    def test_por_genero(self):
        self.assertEqual(stock_por_genero(self.cat), {"Drama": 2, "Romance": 5})

    def test_genero_inexistente(self):
        self.assertEqual(stock_de_genero(self.cat, "Terror"), 0)


if __name__ == "__main__":
    unittest.main()