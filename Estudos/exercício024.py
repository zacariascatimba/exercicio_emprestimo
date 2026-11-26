# Número primo
print('Seja bem vindo\nVamos identificar os números primos')

# numi - Número Inicial
numi = int(input('Digite o primeiro número do intervalo a ser verificado: '))
# numf - Número Final
numf = int(input('Digite o último número do intervalo a ser verificado: '))


for c in range(numi, numf+1):
    if c <= 1:
        print("O número {} não pertence ao conjunto dos números primos.".format(c))
    elif c == 2:
        print("O número {} pertence ao conjunto dos números primos.".format(c))
    elif c % 2 == 0:
        print("O número {} não pertence ao conjunto dos números primos.".format(c))
    else:
        print('O número {} pertence ao conjunto dos números primos.'.format(c))

