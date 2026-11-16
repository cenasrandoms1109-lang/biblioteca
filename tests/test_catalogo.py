from src.livro import Livro
from src.catalogo import catalogo, adicionar_livro, remover_livro

def test_remover_livro():
    catalogo.clear()
    
    livro = Livro("Livro 1", "1234567890")
    
    adicionar_livro(livro)
    
    assert remover_livro("1234567890") == True
    assert len(catalogo) == 0
    
    assert remover_livro("1234567890") == False 