print("Seja bem vindo, caro agente")

velocidade = int(input('Qual a velocidade que o carro estava a percorrer? R: '))

if velocidade > 80:
    multa = (velocidade - 80)*5000
    print('A multa é de {}'.format(multa))
    print('Recomenda-se que se faça o pagamento o mais breve possível')
else:
    print('Continua a ser esse exemplo e andar com prudência. Parabéns!')