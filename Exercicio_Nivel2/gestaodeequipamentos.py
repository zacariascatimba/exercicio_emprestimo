# LISTA DOS EQUPAMENTOS E OS ESTADOS DOS MESMOS
from datetime import date

data = date(2026, 11, 10)

colaboradores = ["Ana Costa", "Carlos Mendes", "Joana Lopes"]

equipamentos = [{"id": "E001",
                 "nome": "Portatil Dell Latitude",
                 "tipo": "Portatil",
                 "estado": "Emprestado"},
                { "id": "E002",
                  "nome": "Projector Epson",
                  "tipo": "Projector",
                  "estado": "Emprestado"},
                {"id": "E003",
                 "nome": "Portatil ProBook",
                 "tipo": "Projector",
                 "estado": "Disponível"},
                {"id": "E004",
                 "nome": "Monitor Samsung 24",
                 "tipo": "Monitor",
                 "estado": "Em reparação"},
                {"id": "E005",
                 "nome": "Portatil Lenovo",
                 "tipo": "Monitor",
                 "estado": "Disponível"}
                ]

emprestimos = [{"id": "E003",
                "colaborador": "Ana Costa",
                "saida": date(2026, 10, 20),
                "devevoltar": date(2026, 10, 25),
                "voltou": date(2026, 10, 24)},
               {"id": "E001",
                "colaborador": "Ana Costa",
                "saida": date(2026, 11, 1),
                "devevoltar": date(2026, 11, 5),
                "voltou": "Ainda não voltou"},
               {"id": "E002",
                "colaborador": "Carlos Mendes",
                "saida": date(2026, 11, 8),
                "devevoltar": date(2026, 11, 12),
                "voltou": "Ainda não voltou"}
               ]



menu = input("MENU"
             "\n1 - VER OS EQUIPAMENTOS E OS ESTADOS"
             "\n2 - EMPRESTAR UM EQUIPAMENTO"
             "\n3 - REGISTAR UMA DEVOLUÇÃO"
             "\n4 - VER EMPRÉSTIMOS EM ATRASO"
             "\n5 - VER QUANTIDADE DE EMPRÉSTIMOS POR COLABORADOR"
             "\n\nPor favor, digite a opção correta (1, 2, 3, 4 ou 5) ou digite 0 para encerrar: ")

while menu != "0":
    if menu == "1":
        for equipamento in equipamentos:
            print(f"Os equipamentos disponíveis são:\nNome: {equipamento['nome']}\nEstado: {equipamento['estado']}")
        seguir = input("\nDeseja ver mais alguma coisa? Se sim, escolha novamente a opção ou digite 0 para encerrar!").upper()
        if seguir == "0":
            break
        elif seguir == "SIM" or seguir == "S":
            menu
        elif seguir != "SIM" and seguir != "S" and seguir != "0":
            opcao = input("Digite a opção correta!")
    elif menu == "2":
        for emprestimo in equipamentos:
            if emprestimo["estado"] == "Disponível":
                idequipamento = input("Por favor, digite o ID do equipamento: ")
                nomecolaborador = input("Por favor, digite o nome do funcionário que iráreceber o equipamento: ")
#               datasaida = input("Insira a data"date)
            emprestimos.append({"id": emprestimo["id"],})

    elif menu == "3":
        print("")

    elif menu == "4":
        print("")

    elif menu == "5":
        print("")

    elif menu == "0":
        print("Programa encerrado")
        break







