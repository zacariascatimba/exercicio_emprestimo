# Números divisíveis por 3
num = int(input('Por favor, digite a quantidade de números que quer analisar: '))
c = 0
for z in range(0, num, 3):
    print(z)
    c += z
print('O somatório de todos os números é: {}'.format(c))