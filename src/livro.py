from dataclasses import dataclass, field
 
 
@dataclass
class Livro:
    """Formato partilhado do livro (ajusta aos campos reais do projeto)."""
    isbn: str
    titulo: str
    autor: str
    generos: list[str] = field(default_factory=list)
    quantidade: int = 0
 
