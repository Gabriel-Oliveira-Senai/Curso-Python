with open("notas.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo guardado no arquivo:")
    print(conteudo)