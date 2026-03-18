from condominios import condominios
from sindicos import sindicos


def pula_linha():
    print("---------------")

# Função para a seleção de opções no menu


def menu():
    while True:
        print("1 - Condomínios")
        print("2 - Unidades")
        print("3 - Síndico")
        print("4 - Despesas")
        print("5 - Sair")

        print("Selecione uma opção: ")

        escolha = int(input())
# cada opção leva a uma função, que foi definida em cada arquivo
        if escolha == 1:
            condominios()
        elif escolha == 2:
            unidades()
        elif escolha == 3:
            sindicos()
        elif escolha == 4:
            despesas()
        elif escolha == 0:
            break
        else:
            pula_linha()
            print(f"A opção {escolha} é inválida")
            pula_linha()


def main():
    menu()


if __name__ == "__main__":
    main()
