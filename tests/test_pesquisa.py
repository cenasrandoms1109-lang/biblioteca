import unittest

from src.livro import Livro
from src.pesquisa import search_by_author, search_by_title

Livros = [
    Livro("111", "Os Maias", "Eça de Queirós", ["Romance"], 3),
    Livro("222", "Memorial do Convento", "José Saramago", ["Romance", "Histórico"], 2),
    Livro("333", "Ensaio sobre a Cegueira", "José Saramago", ["Ficção"], 5),
]


class TestPesquisa(unittest.TestCase):
    def test_titulo_parcial_sem_maiusculas(self):
        self.assertEqual([l.isbn for l in search_by_title(Livros, "maias")], ["111"])

    def test_titulo_sem_resultados(self):
        self.assertEqual(search_by_title(Livros, "xyz"), [])

    def test_termo_vazio(self):
        self.assertEqual(search_by_title(Livros, "  "), [])

    def test_autor_ignora_acentos(self):
        isbns = [l.isbn for l in search_by_author(Livros, "jose saramago")]
        self.assertEqual(isbns, ["222", "333"])

    def test_autor_no_resultados(self):
        self.assertEqual(search_by_author(Livros, "pessoa"), [])


if __name__ == "__main__":
    unittest.main()