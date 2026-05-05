comando = 2

match comando:
    case 1:
        print("Iniciando jogo...")
    case 2:
        print("Carregando jogo salvo...")
    case 3:
        print("Abrindo configurações")
    case _: 
        print("Coamando Invalido! tente novamente")

        