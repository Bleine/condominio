def menu():
    while True:
        print("1 - opção 1")
        print("2 - opção 2")
        print("3 - opção 3")
        print("0 - sair")

        print("Selecione uma opção: ")
        escolha = int(input())

        if escolha == 1:
            opcao_1()
        else:
            break


def opcao_1():
    print("Você escolheu a opção 1")


def main():
    menu()


if __name__ == "__main__":
    main()

























