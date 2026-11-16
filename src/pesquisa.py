def pesquisa():
    pesquisa = input("Digite o termo de pesquisa: ")

    if pesquisa.upper() == "TITULO":
        titulo = input("Digite o título do livro: ")
        print(f"Você selecionou pesquisar por título: {titulo}")
    elif pesquisa.upper() == "AUTOR":
        autor = input("Digite o nome do autor: ")
        

    return pesquisa
