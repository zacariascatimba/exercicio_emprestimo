# Número Secreto

import random

pergunta1 = "Digite a condição correta (Sim ou Nao): "
pergunta2 = str("OBRIGADO POR JOGAR (FIM DO JOGO)!\n------------------------------------------------\nDeseja jogar novamente? (Sim ou Nao): ")
pergunta3 = "Por favor, digite o seu número (No intervalo de 0 à 20): "
resposta1 = "Este foi o número escolhido pelo computador: {}"
afirmacao1 = "E pela tua sorte, o maior número é o teu. Parabéns pela vitória!"
afirmacao2 = "Infelizmente o computador escolheu o maior número. Lamento"

def opcao1():
    computador = random.choice(range(1, 21))
    num = int(input(pergunta3))
    print(resposta1.format(computador))
    while 0 <= num <= 20:
        if num == computador:
            print("Temos um empate!")

        elif num != computador:
            print("Os números são diferentes!")
            if num > computador:
                print(afirmacao1)

            elif num < computador:
                print(afirmacao2)

        num = int(input(pergunta3))

condicao = ""
condicao2 = ""
allow_value = ["SIM", "NAO", "S", "N"]
while True:
    condicao = input("Vamos jogar? (Sim ou Nao): ").upper() if condicao == ""  else condicao2
    if condicao == "SIM" or condicao == "S":
        opcao1()
    elif condicao == "NAO" or condicao == "N":
        print("Finalizando...")
        break

    elif condicao not in  ["SIM", "NAO", "S", "N"]:
        condicao2 = input(pergunta1).upper()


