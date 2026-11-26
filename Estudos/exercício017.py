import random

print('VAMOS JOGAR')

computador1 = random.choice(['Pedra', 'Papel', 'Tesoura'])
# ppt - Pedra, Papel ou Tesoura
ppt1 = input('Vamos lá\nEscolha entre Pedra, Papel ou Tesoura? R: ')
print('Esta foi a resposta do computador: {}'.format(computador1))

ppt = ppt1.upper()
computador = computador1.upper()

while computador != ppt:
#    if computador == ppt:
#        print('Assim sendo, é um empate!')'''
    if ppt == 'PEDRA':
        if computador == 'PAPEL': print('Que pena, a vitória é do computador!')
        elif computador == 'TESOURA': print('Parabens! A vitória é tua!')

    elif ppt == 'PAPEL':
        if computador == 'PEDRA': print('Parabéns, a vitória é tua!')
        elif computador == 'TESOURA': print('Que pena, a vitória é do computador!')

    elif ppt == 'TESOURA':
        if computador == 'PEDRA': print('Que pena, a vitória é do computador!')
        elif computador == 'PAPEL': print('Parabéns, a vitória é tua!')

    else: print('Escolha a opção correta (Pedra, Papel ou Tesoura). Obrigado!')
    break
