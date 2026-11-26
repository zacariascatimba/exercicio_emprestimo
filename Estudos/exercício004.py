idade = int(input("Quantos anos tens? R: "))

if idade <= 4: print("Tu és um bebê")

elif idade >= 5 and idade < 12: print("Tu és uma criança")

elif idade >= 12 and idade < 18: print("Tu és um adolescente")

elif idade >=18 and idade < 45: print("Tu és um jovem")

elif idade >=45 and idade < 59: print("Tu és um senhor")

elif idade >=59 and idade < 89: print("Tu és um idoso")

elif idade >= 89:
    print("Superaste as expectativas de vida de um idoso")
    print("Qual é o segredo dessa idade")