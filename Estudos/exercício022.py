# Tabuada
print('Seja bem vindo')
# numcal - Numero a ser calculado
numcal = int(input('Gostarias de vizualizar a tabuada de qual número? R: '))
# numtab - Quantidade da tabuada
numtab = int(input('Até qual número gostarias que fosse calculado? R: '))
sinal = input('Qual sinal de operação gostarias de calcular na nossa tabuada? R: ')

if sinal == 'Adicao' or sinal == 'adicicao' or sinal == 'mais' or sinal == 'Mais':
    for c in range(0, numtab+1):
        resultado = numcal + c
        print('O resultado da adição de {} + {} = {}'.format(numcal, c, resultado))
    print('\nParabéns, chegaste ao fim da tua tabuada!')

elif sinal == 'Subtracao' or sinal == 'subtracao' or sinal == 'menos' or sinal == 'Menos':
    for c in range(0, numtab+1):
        resultado = numcal - c
        print('O resultado da subtração de {} - {} = {}'.format(numcal, c, resultado))
    print('\nParabéns, chegaste ao fim da tua tabuada!')

elif sinal == 'Multiplicacao' or sinal == 'multiplicacao' or sinal == 'vezes' or sinal == 'Vezes':
    for c in range(0, numtab+1):
        resultado = numcal * c
        print('O resultado da multiplicação de {} x {} = {}'.format(numcal, c, resultado))
    print('\nParabéns, chegaste ao fim da tua tabuada!')

elif sinal == 'Divisao' or sinal == 'divisao':
    for c in range(0, numtab+1):
        resultado = numcal / c
        print('O resultado da divisão de {} / {} = {}'.format(numcal, c, resultado))
    print('\nParabéns, chegaste a tua tabuada!')

else: print('Digite um sinal de operação verdadeiro (Adicao, Subtracao, Multiplicacao ou Divisao)')

