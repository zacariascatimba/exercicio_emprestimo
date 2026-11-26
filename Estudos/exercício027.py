import random

numero = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
valor = int(input('Digite o teu número para tentar adivinhar se está próximo do número escolhido pelo computador: '))
print('A escolha do computador é de: {}'.format(numero))
while numero != valor:
    numero = int(input('Digite por favor o teu número novamente: '))
    if numero > valor:
        print(' - Estás acima do número esperado, tente mais\n')
    elif numero < valor:
        print(' - Estás abaixo do número esperado, tente mais\n')
    elif numero == valor:
        print('Terminou')
        break
