numero = int(input('Digite um número abaixo e eu direi se é Par ou Ímpar\nR: '))

if numero % 2 == 0:
    print('O número {} é par'.format(numero))
elif numero % 2 != 0:
    print('O número {} é ímpar'.format(numero))