print('Seja Bem-Vindo')
nome = input('Digite o seu nome: ')
pruduto = input('Digite o nome do produto desejado: ')
preco = float(input('Digite o valor do produto: '))
#print('Digite a forma de pagamento:\n1 - Espécie\n2 - Cartão\n3 - Cheque')
formapag = input('Digite a condição de pagamento (vista, parcelado): ')
if formapag == 'Vista' or formapag == 'vista':
    # dinche - Dinheiro e Cheque
    dinche = input('A forma d epagamento será a dinheiro/cheque ou cartao? R: ')
    if dinche == 'Dinheiro' or dinche == 'dinheiro' or dinche == 'Cheque' or dinche == 'cheque':
        print('Nesta condição, terás um desconto de 10% do valor do produto')
        desconto = preco - ((preco * 10) / 100)
        print('Assim sendo, ao invés de pagar {}kz, vais pagar {}kz pelo produto desejado'.format(preco, desconto))

    elif dinche == 'Cartao' or dinche == 'cartao':
        print('Nesta condição, terás um desconto de 5% do valor do produto')
        desconto = preco - ((preco * 5) / 100)
        print('Assim sendo, ao invés de pagar {}kz, vais pagar {}kz pelo produto desejado'.format(preco, desconto))

elif formapag == 'Parcelado' or formapag == 'parcelado':
    print('Nesta condição, terás que colocar a quantidade das vezes que desejas parcelar!')
    parcela = int(input('Vais querer parcelar quantas vezes? R: '))
    if parcela <=2:
        print('Nesta condição, não terás desconto ou uma taxa adicional. Vais pagar o produto no preço original, que é de {}kz.'.format(preco))
    elif parcela > 2:
        print('Nesta situação, terás que pagar mais 20% do valor de cada parcela.')
        valorparcela = (preco / parcela)
        taxa = (valorparcela * 0.2) + valorparcela
        valorapagar = (taxa * parcela)
        print('Sendo assim, o produto custa {}kz e parcelando em {} vezes cada parcela vai sair a {}kz, totalizando assim {}kz. Obirgado!'.format(preco, parcela, taxa, valorapagar))

