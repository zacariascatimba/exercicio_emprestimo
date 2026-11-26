print('Vamos fazer um jogo!')
nome = input('Como te chamas? R: ')
print('Muito bem {}, o jogo consiste em digitares um número abaixo e tentar adivinhar se este número se encontra no intervalo de números que eu preparei'.format(nome))
num = int(input('Qual o seu número? R: '))
if num > 5:
    print("O seu número está fora do intervalo")
else:
    print("Parabéns, selecionaste o número correro")