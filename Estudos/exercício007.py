genero = input('Quano teu gênero? R: ')
if genero == 'Masculino':
    nome = input("Saudações, prezado\nQual é o seu nome? R: ")
elif genero == 'Feminino':
    nome = input("Saudações, prezada\nQual é o seu nome? R: ")

else: print("Por favor, digite o gênero correto. Obrigado!\n", breakpoint())

num1 = int(input('Qual a tua nota do primeiro semestre? R: '))
num2 = int(input('Qual a tua nota do segundo semestre? R: '))
prisem = num1 * 0.3
segsem = num2 * 0.7

media = (prisem + segsem)

print('Parabens! A sua média é de {} valores'.format (round(media)))

if media <= 7:
    print('Infelizmente estás reprovado')
elif media >= 7.1 and media <= 9.9:
    print('Terás que fazer o exame de recurso')
elif media <= 10 and media >= 13.9:
    print('Aprovaste, mas precisas melhorar este resultado')
elif media >= 14 and media <= 20:
    print('Aprovaste, mantenha o foco')