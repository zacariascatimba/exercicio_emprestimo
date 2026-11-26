print(':'*36)
print('Seja bem vindo ao Exército Angolano')
print(':'*36,'\n')

# regobri - Regime Obrigatório
regobri = 5
genero = input('Qual é o teu gênero? (Masculino ou Feminino): ')
if genero == 'Masculino' or genero == 'M' or genero == 'm':
    nome = input('Digite o seu nome, prezado: ')
    idade = int(input('Quantos anos tens, caríssimo {}: '.format(nome)))

    if idade < 18:
        print('Ainda não chegou o tempo de se alistares, podes voltar para casa e voltar assim que completares 18 anos!')

    elif idade >= 18 and idade <= 35:
        idadecerta = input('Já se alistaste? (Sim ou Nao): ')

        if idadecerta == 'Sim' or idadecerta == 'S' or idadecerta == 's':
            print('Parabés, fizeste a melhor escolha. Boa sorte!')
            tempo = int(input('Há quantos anos estás no regime obrigatório? R: '))
            # tempos - Tempo de serviço
            tempos = regobri - tempo
            print('Muito bem caríssiomo {}, te restam {} anos de serviço. Daqui a nada termina.'.format(nome, tempos))

        elif idadecerta == 'Nao' or idadecerta == 'N' or idadecerta == 'n':
            print('Estás a espera de quê? Vai lá e cumpre o regime obrigatório de 5 anos.\nVai se cadastrar logo')

    elif idade > 35 and idade <= 59:
        # Cumpriu o Serviço
        cumprius = input('Cumpriste o regime militar obrigatório? (Sim ou Nao): ')

        if cumprius == 'Sim' or cumprius == 'S' or cumprius == 's':
            print('Parabéns, podes ir para casa e continuar a descansar!')

        elif cumprius == 'Nao' or cumprius == 'N' or cumprius == 'n':
            print('Deves se dirigir agora para um Distrito de Recrutamento Militar mais próximo o mais breve possível!')

    elif idade > 59:
        print('Podes seguir, caríssimo veterano da Pátria.')

elif genero == 'Feminino' or genero == 'F' or genero == 'f':
    nome = input('Como te chamas, senhora? R: ')
    print('Podes ir para casa, senhora {}'.format(nome))

else:
    print('Digite o gênero corretamente, por favor!')




