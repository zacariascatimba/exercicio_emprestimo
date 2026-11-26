nome = input("Vamos calcular o preço da viagem!\nPor favor, digite o seu nome: ")

kmp = int(input('Quantos quilometros percorreste? R: '))
if kmp <= 200:
    preco = kmp * 500
    print('A tarifa nesta rota é de 500 kz por quilometro\nSendo assim, o valor total a pagar é de: {}'.format(preco))
else:
    preco = kmp * 700
    print = ('A tarifa nesta rota é de 700 kz por quilómetro\nSendo assim, o valor a pagar é de: {}'.format(preco))

print("Muito obrigado prezado(a) {} e volte sempre!".format(nome))