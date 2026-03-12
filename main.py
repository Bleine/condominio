from condominios import condominios
from sindicos import sindicos


def menu():
    while True:
        print("1 - Condomínios")
        print("2 - Unidades")
        print("3 - Síndico")
        print("0 - Despesas")

        print("Selecione uma opção: ")
        escolha = int(input())

        if escolha == 1:
            condominios()
        elif escolha == 3:
            sindicos()

        else:
            break


def main():
    menu()


if __name__ == "__main__":
    main()
