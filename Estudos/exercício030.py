# Número Secreto

import random

pergunta1 = "Digite a condição correta (Sim ou Nao): "
pergunta2 = "\nDeseja jogar novamente? (Sim ou Não): "
resposta1 = "Este foi o número escolhido pelo computador: {}"
afirmacao1 = "E pela tua sorte, o maior número é o teu. Parabéns pela vitória!"
afirmacao2 = "\nInfelizmente o computador escolheu o maior número. Lamento"

condicao = input("Vamos jogar? (Sim ou Não): ").upper()
while condicao == "SIM" and "S" or condicao == "NAO" and "N" or condicao != "SIM" or condicao != "NAO":
    if condicao == "SIM" or condicao == "S":
        computador = random.choice(range(1, 21))
        num = int(input("Por favor, digite o seu número: "))
        print(resposta1.format(computador))
        if num == computador:
            print("Temos um empate!")
            condicao = input(pergunta2).upper()
            if condicao == "SIM" or condicao == "S":
                computador = random.choice(range(1, 21))
                num = int("Por favor, digite o seu número")
                print(resposta1.format(computador))
            elif condicao == "NAO" or condicao == "N":
                print("Finalizando...")
                break
            elif condicao != "SIM" or condicao != "NAO":
                condicao = input(pergunta1).upper()

        elif num != computador:
            print("Os números são diferentes!")
            if num > computador:
                print(afirmacao1)
                condicao = input(pergunta2).upper()
                if condicao == "SIM" or condicao == "S":
                    computador = random.choice(range(1, 21))
                    num = int("Por favor, digite o seu número")
                    print(resposta1.format(computador))
                elif condicao == "NAO" or condicao == "N":
                    print("Finalizando...")
                    break
                elif condicao != "SIM" or condicao != "NAO":
                    condicao = input(pergunta1).upper()
            if num < computador:
                print(afirmacao2)
                condicao = input(pergunta2).upper()
                if condicao == "SIM" or condicao == "S":
                    computador = random.choice(range(1, 21))
                    num = int("Por favor, digite o seu número")
                    print(resposta1.format(computador))
                elif condicao == "NAO" or condicao == "N":
                    print("Finalizando...")
                    break
                elif condicao != "SIM" or condicao != "NAO":
                    condicao = input(pergunta1).upper()


    elif condicao == "NAO" or condicao == "N":
        print("Finalizando...")
        break
    elif condicao != "SIM" or condicao != "NAO":
        condicao = input(pergunta1).upper()














