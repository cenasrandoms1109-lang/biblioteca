from dataclasses import dataclass, field


@dataclass
class Livro:
    isbn: str
    titulo: str
    autor: str
    generos: list[str] = field(default_factory=list)
    quantidade: int = 0