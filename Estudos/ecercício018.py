import random
from multiprocessing.resource_sharer import stop

print('Seja Bem-Vindo\nVamos jogar?')

computador = int(random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))
pessoa = int(input('Por favor, digite um número no intervalo de 0 a 10: '))
if pessoa > 10 or pessoa < 0:
    print('Por favor, escolha um número entre 0 e 10!')

print('Esta foi a escolha do computador {}'.format(computador))

if pessoa == computador:
    print('Foi um empate, parabéns aos dois!')
elif pessoa > computador:
    print('Parabéns, a vitória é tua. O computador perdeu!')
elif pessoa < computador:
    print('Infelizmente perdeste. A vitória é do computador!')
