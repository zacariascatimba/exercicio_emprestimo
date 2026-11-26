from email import message_from_binary_file

nome = input('Qual é o seu nome? R: ')
genero = input('Qual é o teu gênero? R: ')
dia = input('Qual é o seu dia de nascimento? R: ')
mes = input('Qual é o seu mẽs de aniversário? R: ')
ano = input('Qual é o seu ano de nascimetno? R: ')

if genero == 'Masculino':
    print("Olá,", nome,",é um prazer em te conhecer!\nNasceste no dia", dia,"de", mes,"de", ano,", de acordo, prezado")
elif genero == 'Feminino':
    print("Olá,", nome,",é um prazer em te conhecer!\nNasceste no dia", dia,"de", mes,"de", ano,", de acordo, prezada")

else: print("Certifica-se que estás a colocar o gênero correto!\nSó poder Masculino ou Feminino")