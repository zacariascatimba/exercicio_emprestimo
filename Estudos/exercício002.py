import math
#exercício1: quantidade de salário a receber
nome = input("Como te chamas? ")
print("Muito bem, " , nome)

salario = int(input("Agora nos diz quanto ganhas? "))
print("Anotamos o teu salário \nQual é a tua dúvida? ")
meses = int(input("Quaro saber qunato ganho num certo intervalo de tempo \nQuantos meses queres analisar? "))
print()
mesesdetrabalho = (salario * meses)
print("Prezado (a)" , nome , ", o teu salário no intervalo dos meses solicitados é de: ", mesesdetrabalho)



