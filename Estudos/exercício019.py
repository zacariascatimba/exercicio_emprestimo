print('Vamos lançar o fogo de artifício')
aviso = input('Vamos começar? (Sim ou Nao) R: ')
if aviso == 'Sim' or aviso == 'sim':
    for c in range(10, -1, -1):
        print(c)
    print('Feliz ano novo!')
elif aviso == 'Nao' or aviso == 'nao':
    print('Sem problemas, pode voltar quando quiser!')
