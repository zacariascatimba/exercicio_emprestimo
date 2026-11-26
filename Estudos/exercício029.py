# contagem dos números ímpar ou par

num = int(input("Por favor, digite um número: "))
par = 0
impar = 0

while num != 0:
    if num % 2 == 0:
        par += 1
        if par > 1:
            print
    if num % 2 == 1:
        impar += 1

    num = int(input("Digite outro número ou digite 0 para terminar o programa: "))

if par > 1:
    print("No total tem {} números pares".format(par))
else:
    print("No total tem {} numero par".format(par))
if impar > 1:
    print("No total tem {} números ímpares".format(impar))
else:
    print("No total tem {} número ímpar".format(impar))

