print('Chegou o momento mais esperado po todos.')
salario = int(input('Qual é o teu salário? R: '))

if salario >= 500000:
    aumento = ((salario * 0.1) + salario)
    print('Parabens, recebeste um aumento de 10%, agora tens um salário de {} kwanzas'.format(aumento))
else:
    aumento = ((salario * 0.15) + salario)
    print('Parabens, recebeste um aumento de 15%, agora tens um salário de {} kwanzas'.format(aumento))
