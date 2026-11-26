print('Seja Bem-Vindo')
x = 0
for c in range(1, 7):
    num = int(input('Por favor, digitr um número: '))
    if num % 2 == 0:
        x += num
    elif num % 2 != 0:
        print('O número {} é ímpar. Sendo assim, não entrará no somatório.'.format(num))
print('O somatório dos números pares é igual a: {}'.format(x))
if x == 0:
    print('Infelizme não verificamos a existência de um número par. Tente de novo.')



