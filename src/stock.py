def take_books_by_gender(books, isbn: str):
    """US9: devolve a lista de géneros do livro com esse ISBN.

    Devolve None se o livro não existir.
    """
    for book in books:
        if book.isbn == isbn:
            return list(book.gender)
    return None