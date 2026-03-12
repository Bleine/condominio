import sqlite3


def sindicos():
    while True:
        print("Você selecionou a opção Síndicos")
        print("Opção 1 - Criar \n",  "Opção 2 - Ler \n",
              "Opção 3 - Atualizar \n", "Opção 4 - Deletar \n", "Opção 0 - Voltar \n")

        escolha = int(input("Escolha uma opção: "))

        match escolha:
            case 1:
                print("CREATE")
            case 2:
                conn = sqlite3.connect("condominios.db")
                cursor = conn.cursor()
                res = cursor.execute("SELECT * FROM sindicos LIMIT 10")
                show = res.fetchall()
                for linha in show:
                    print(linha)
            case 3:
                print("UPDATE")
            case 4:
                print("DELETE")
            case 0:
                break
