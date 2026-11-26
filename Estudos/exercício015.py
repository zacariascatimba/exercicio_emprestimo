print('Seja Bem-Vindo\nVamos calcular o índice de massa corporal')

nome = input('Por favor, digite o seu nome: ')
peso = float(input('Por favor, digite o seu peso: '))
altura = float(input('Por favor, digite a sua altura: '))
# Índice da Massa Corporal
imc = peso / altura**2
if imc < 18.5:
    print('Olá, {}. O teu índice de massa corporal é de: {}. Arredondando passa para: {}'.format(nome, imc, round(imc)))
    print('Sengundo a OMS - Organização Mundial da Saúde, estás abaixo do peso ideal')
    print('NÍVEL DE PRIORIDADE: ALTA')

elif imc >= 18.5 and imc <= 24.9:
    print('Olá, {}. O teu índice de massa corporal é de: {}. Arredondando passa para: {}'.format(nome, imc, round(imc)))
    print('Segundo a OMS - organização Mundial da Saúde, estás com o peso Adequado (Normal)')
    print('NÍVEL DE PRIORIDADE: BAIXA')

elif imc >= 25.0 and imc <= 29.9:
    print('Olá, {}. O teu índice de massa corporal é de: {}. Arredondando passa para: {}'.format(nome, imc, round(imc)))
    print('Segundo a OMS - Organização Mundial da Saúde, estás com Sobrepeso')
    print('NÍVEL DE PRIORIDADE: MÉDIA')

elif imc >= 30.0 and imc <= 34.9:
    print('Olá, {}. O teu índice de massa corporal é de: {}. Arredondando passa para: {}'.format(nome, imc, round(imc)))
    print('Segundo a OMS - Organização Mundial da Saúde, estás com Obesidade do Primeiro Grau')
    print('NÍVEL DE PRIORIDADE: ALTA')

elif imc >= 35.0 and imc <= 39.9:
    print('Olá, {}. O teu índice de massa corporal é de: {}'.format(nome, imc))
    print('Segundo a OMS - Organização Mundial da Saúde, estás com Obesidade do Segundo Grau')
    print('NÍVEL DE PRIORIDADE: ALTA')

elif imc > 40.0:
    print('Olá, {}. O teu índice de massa corporal é de: {}'.format(nome, imc))
    print('Segundo a OMS - Organização Mundial da Saúde, estás com Obesidade do Terceiro Grau (Grave)')
    print('NÍVEL DE PRIORIDADE: ALTA')



