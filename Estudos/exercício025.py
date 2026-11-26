senha = 'Angola'
passe = input('Por favor, digite a tua palavra passe: ')

'''if senha == passe:
    print('Login efectuado com sucesso!')'''
if senha != passe:
    for c in range(1, 3):
        print('Palavra passe errada, tente novamente!')
        tentativa = input('Tentativa número {}. Por favor, digite novamente a palavra passe: '.format(c+1))
        if senha == passe:
            print('Login efectuado com sucesso!')
    print('Conta bloqueada, contacte o administrador!')



