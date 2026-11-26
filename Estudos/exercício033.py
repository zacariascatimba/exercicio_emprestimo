import random

pergunta1 = "Digite a condição correta (Sim ou Nao): "
pergunta2 = str("OBRIGADO POR JOGAR (FIM DO JOGO)!\n------------------------------------------------\nDeseja jogar novamente? (Sim ou Nao): ")
pergunta3 = "Por favor, digite o seu número (No intervalo de 0 à 20): "
resposta1 = "Este foi o número escolhido pelo computador: {computador}"
afirmacao1 = "E pela tua sorte, o maior número é o teu. Parabéns pela vitória!"
afirmacao2 = "Infelizmente o computador escolheu o maior número. Lamento"

condicao = input("Vamos jogar? (Sim ou Nao): ").upper()

def opcao1():
    computador = random.choice(range(1, 21))
    num = int(input(pergunta3))
    print(resposta1.format(computador))
    if num == computador:
        print("Temos um empate!")

    elif condicao == "SIM" or condicao == "S":
        computador = random.choice(range(1, 21))
        nun = int(input(pergunta3))
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
                num = int(input(pergunta3))
                print(resposta1.format(computador))
            elif condicao == "NAO" or condicao == "N":
                print("Finalizando...")
                break
            elif condicao != "SIM" or condicao != "NAO":
                condicao = input(pergunta1).upper()
        elif num < computador:
            print(afirmacao2)
            condicao = input(pergunta2).upper()
            if condicao == "SIM" or condicao == "S":
                computador = random.choice(range(1, 21))
                num = int(input(pergunta3))
                print(resposta1.format(computador))
            elif condicao == "NAO" or condicao == "N":
                print("Finalizando...")
                break
            elif condicao != "SIM" or condicao != "NAO":
                condicao = input(pergunta1).upper()

def opcao2():
    print("Finalizando...")

def opcao3():
    condicao = input(pergunta1).upper()

while True:
    condicao2 = input("Deseja jogar novamente? (Sim ou Nao): ").upper()
    if condicao == "SIM" or condicao == "S" or condicao2 == "SIM" or condicao2 == "S":
        opcao1()
    elif condicao == "NAO" or condicao == "N" or condicao2 == "NAO" or condicao2 == "N":
        opcao2()
    elif condicao != "SIM" or condicao != "NAO" or condicao != "S" or condicao != "N" or condicao2 == "SIM" or condicao2 == "NAO" or condicao != "S" or condicao2 == "N":
        opcao3()