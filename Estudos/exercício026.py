import math

x1 = 1
x2 = 1
while x1 != 0 and x2 !=0:
    valora = float(input('Qual é o valor de A? R: '))
    valorb = float(input('Qual é o valor de B? R: '))
    valorc = float(input('Qual é o valor de C? R: '))
    delta = ((valorb**2) - 4 * valora * valorc)
    raiz = math.sqrt(delta)
    x1 = ((-valorb + raiz) / 2 * valora)
    x2 = ((-valorb - raiz) / 2 * valora)
    print('Quando:\nA = {}\nB = {}\nC = {}\nO valor de X1 = {} e o valor de X2 = {}'.format(valora, valorb, valorc, x1, x2))
print('Chegou ao final')