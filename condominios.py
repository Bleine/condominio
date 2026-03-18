def condominios():
    while True:
        print("Você selecionou a opção CONDOMÍNIOS")
        print("Opção 1 - Criar \n",  "Opção 2 - Ler \n",
              "Opção 3 - Atualizar \n", "Opção 4 - Deletar \n", "Opção 0 - Voltar \n")
        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Escolha não é um inteiro")
        else:
            match escolha:
                case 1:
                    print("CREATE")
                case 2:
                    print("READ")
                case 3:
                    print("UPDATE")
                case 4:
                    print("DELETE")
                case 0:
                    break
