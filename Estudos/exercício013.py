print('='*25)
print('Seja bem-vindo ao Banco')
print('='*25)

nome = input('Qual é o teu nome? R: ')
salario = int(input('Qual é o teu salário? R: '))
valordacasa = int(input('Quanto custa a casa que queres comprar? R: '))
tempopagamento = int(input('Em quanto tempo gostarias de pagar? R: '))
prestacaodacasa = (round(valordacasa / tempopagamento))
percentagemdosalario = (round(salario * 0.3))

if prestacaodacasa > percentagemdosalario:
    print('Infelizmente não podes receber um emprestimo')
    print('Isso porque 30% do teu salário equivale a {}kz e é inferior a {}kz que se determina como o valor da prestação'.format(percentagemdosalario, prestacaodacasa))
elif percentagemdosalario >= prestacaodacasa:
    print('Parabéns, foste aprovado para receber o empréstimo')
    sugestao = (round(valordacasa/percentagemdosalario))
    diferencadosalario = (salario - (sugestao * percentagemdosalario))
    print('Analisando o teu salário, tu podes pagar a casa num intervalo de {} meses e não em {} meses como colocaste na tua solicitação'.format(sugestao, tempopagamento))
    print('Nota:\nDescontando os {}kz que correspondem aos 30% do teu salário que serão descontados, vais sobrar com aproximadamente {}kz do teu salário em cada mês'. format(percentagemdosalario, diferencadosalario))