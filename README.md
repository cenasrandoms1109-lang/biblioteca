# Biblioteca

É uma aplicação em python para a gestão de uma biblioteca que permite registar, editar , remover, pesquisar livros e consultar o stock.

## Funcionalidades

Userstories definidas no backlog e aceites para o TP2:

- Registar um livro (com validação do titulo, autor e ISBN)
- Editar os dados de um livro 
- Remover um livro do catálogo
- Impedir ISBN duplicados
- Pesquisar livros por título
- Pesquisar livros por autor
- Pesquisar livros por ISBN
- Ver o stock total de livros por género
- Saber os géneros de um livro

## Requisitos

- Git
- Python

## Como executar

```bash
git clone https://github.com/cenasrandoms1109-lang/biblioteca.git
cd biblioteca
py main.py
```

## Como correr os testes

```bash
python -m unittest tests.test_catalogo -v
```

Cada ficheiro de testes corre-se da mesma maneira, trocando apenas o nome do módulo (ex: tests.test_pesquisa).

## Estrutura do projeto

```
biblioteca/
├── main.py              # ponto de entrada da aplicação
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── livro.py         # formato dos dados de um livro
│   ├── catalogo.py      # registar, editar e remover livros
│   ├── pesquisa.py      # pesquisa por título, autor e ISBN
│   ├── stock.py         # stock por género e géneros de um livro
│   ├── armazenamento.py # guardar e carregar os dados em ficheiro
│   └── menu.py          # menus da consola
├── tests/               # testes automáticos (unittest)
├── data/                # ficheiros de dados
└── docs/                # documentação gerada
```

## Equipa

- Diogo Caetano
- Gonçalo Losada
- João Pedro Balbino
- Kristian Saraiva