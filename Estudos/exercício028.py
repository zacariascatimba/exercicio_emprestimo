print('Seja Bem-Vindo')
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
x = '0'

print("OPÇÕES:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Maior e o Menor\n6 - Digitar novos números\n7 - Sair do Programa")
opcao = input("\nPor favor, escolha uma das opções acima (Adicione apenas o número): ")

while x >= '1' or x <= '7':
    if opcao == '1':
        resultado = num1 + num2
        print("O resultado da adicção de {} + {} = {}".format(num1, num2, resultado))
        opcao = input("Deseja escolher novamente uma opção?\nSe sim, escolha novamente\nSe não, clica em 0 para parar\nObrigado. R: ")
    elif opcao == '2':
        resultado = num1 - num2
        print("O resultado da subtração de {} - {} = {}".format(num1, num2, resultado))
        opcao = input("Deseja escolher novamente uma opção?\nSe sim, escolha novamente\nSe não, clica em 0 para parar\nObrigado. R: ")
    elif opcao == '3':
        resultado = num1 * num2
        print("O resultado da multiplicação de {} * {} = {}".format(num1, num2, resultado))
        opcao = input("Deseja escolher novamente uma opção?\nSe sim, escolha novamente\nSe não, clica em 0 para parar\nObrigado. R: ")
    elif opcao == '4':
        resultado = num1 / num2
        print("O resultado da divisão de {} / {} = {}".format(num1, num2, resultado))
        opcao = input("Deseja escolher novamente uma opção?\nSe sim, escolha novamente\nSe não, clica em 0 para parar\nObrigado. R: ")
    elif opcao == '5':
        if num1 > num2:
            print("O maior número é: {}".format(num1))
        else:
            print("O maior número é: {}".format(num2))
        opcao = input("Deseja escolher novamente uma opção?\nSe sim, escolha novamente\nSe não, clica em 0 para parar\nObrigado. R: ")
    elif opcao == '6':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        opcao = input("Deseja escolher novamente uma opção?\nSe sim, escolha novamente\nSe não, clica em 0 para parar\nObrigado. R: ")
    elif opcao == '0' or opcao >= '7':
        print("Finalizando...")
        break





