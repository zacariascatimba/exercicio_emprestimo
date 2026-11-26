# LISTA DOS EQUPAMENTOS E OS ESTADOS DOS MESMOS
from datetime import date, datetime

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
def listadequipamentos ():
    print("\n================ LISTA DE EQUIPAMENTOS ================")
    print(f"{'CÓDIGO':<10}{'NOME':<25}{'TIPO':<15}{'ESTADO':<15}")
    print("-" * 65)
    for equipamento in equipamentos:
        print(f"{equipamento['id']:<10}{equipamento['nome']:<25}{equipamento['tipo']:<15}{equipamento['estado']:<15}")

def emprestarequipamento():

    print("\n========== REGISTAR EMPRÉSTIMO ==========")

    id = input("Introduza o código do equipamento: ").upper()

    equipamentoencontrado = None

    for equipamento in equipamentos:
        if equipamento["id"] == id:
            equipamentoencontrado = equipamento
            break

    if equipamentoencontrado is None:
        print("Erro: equipamento não encontrado!")

    elif equipamentoencontrado["estado"] != "Disponível":
        print("Erro: este equipamento não está disponível!")
        print("Estado atual:", equipamentoencontrado["estado"])

    else:
        colaborador = input("Nome do colaborador: ")
        if colaborador not in colaboradores:
            print("Erro: colaborador não encontrado!")

        else:
            data_saida = input("Data de saída (DD/MM/AAAA): ")
            data_prevista = input("Data prevista de devolução (DD/MM/AAAA): ")

            try:
                datasaida = datetime.strptime(data_saida, "%d/%m/%Y")
                dataprevista = datetime.strptime(data_prevista, "%d/%m/%Y")

                if dataprevista < datasaida:
                    print("Erro: a data de devolução não pode ser anterior à data de saída!")

                else:
                    novoemprestimo = {
                        "id": id,
                        "colaborador": colaborador,
                        "saida": datasaida,
                        "devevoltar": dataprevista,
                        "voltou": None
                    }
                    emprestimos.append(novoemprestimo)
                    equipamentoencontrado["estado"] = "Emprestado"

                    print("\nEmpréstimo registado com sucesso!")
                    print("Equipamento:", equipamentoencontrado["nome"])
                    print("Colaborador:", colaborador)
                    print("Data de saída:", datasaida)
                    print("Data prevista de devolução:", dataprevista)

            except ValueError:
                print("Erro: introduza datas válidas no formato DD/MM/AAAA.")

def registardevolucao():

    print("\n========== REGISTAR DEVOLUÇÃO ==========")
    id = input("Introduza o código do equipamento: ").upper()

    equipamentoencontrado = None

    for equipamento in equipamentos:
        if equipamento["id"] == id:
            equipamentoencontrado = equipamento
            break

    if equipamentoencontrado is None:
        print("Erro: equipamento não encontrado!")

    else:
        emprestimoencontrado = None

        for emprestimo in emprestimos:
            if emprestimo["devevoltar"] == id and emprestimo["devevoltar"] is None:
                emprestimoencontrado = emprestimo
                break

        if emprestimoencontrado is None:
            print("Erro: não existe um empréstimo activo para este equipamento!")

        else:
            devevoltar = input("Introduza a data de devolução (DD/MM/AAAA): ")

            try:
                datetime.strptime(devevoltar, "%d/%m/%Y")
                emprestimoencontrado["devevoltar"] = devevoltar

                equipamentoencontrado["estado"] = "Disponível"

                print("\nDevolução registada com sucesso!")
                print("Equipamento:", equipamentoencontrado["nome"])
                print("Colaborador:", emprestimoencontrado["colaborador"])
                print("Data de devolução:", devevoltar)
                print("Estado actual: Disponível")

            except ValueError:
                print("Erro: introduza uma data válida no formato DD/MM/AAAA.")

def emprestimosematraso():
    print("\n========== EMPRÉSTIMOS EM ATRASO ==========")
    dataactual = data

    atrasosencontrados = 0

    for emprestimo in emprestimos:
        if emprestimo["devevoltar"] is None:
            dataprevista = date(emprestimo["devevoltar"], "%d/%m/%Y")

            if dataprevista < dataactual:

                atrasosencontrados += 1

                print("\n--------------------------------")
                print("Equipamento:", emprestimo["equipamento"])
                print("Colaborador:", emprestimo["colaborador"])
                print("Data de saída:", emprestimo["data_saida"])
                print("Data prevista:", emprestimo["data_prevista"])
                print("Estado: EM ATRASO")

    if atrasosencontrados == 0:
        print("Não existem empréstimos em atraso.")

    else:
        print("\nTotal de empréstimos em atraso:", atrasosencontrados)

def totalemprestimos():
    print("\n========== EMPRÉSTIMOS POR COLABORADOR ==========")
    for colaborador in colaboradores:
        totalemprestimos = 0

        for emprestimo in emprestimos:
            if emprestimo["colaborador"] == colaborador:
                totalemprestimos += 1
        print(f"Colaborador: {colaborador}")
        print(f"Total de empréstimos: {totalemprestimos}")


while True:
    menu = input(
    "\n========== MENU PRINCIPAL =========="
    "\n1 - VER OS EQUIPAMENTOS E OS ESTADOS"
    "\n2 - EMPRESTAR UM EQUIPAMENTO"
    "\n3 - REGISTAR UMA DEVOLUÇÃO"
    "\n4 - VER EMPRÉSTIMOS EM ATRASO"
    "\n5 - VER QUANTIDADE DE EMPRÉSTIMOS POR COLABORADOR"
    "\n0 - ENCERRAR PROGRAMA"
    "\n\nEscolha uma opção (1, 2, 3, 4 ou 5) ou digite 0 para encerrar: "
    )

    if menu == "1":
        listadequipamentos()

    elif menu == "2":
        emprestarequipamento()

    elif menu == "3":
        registardevolucao()

    elif menu == "4":
        emprestimosematraso()

    elif menu == "5":
        totalemprestimos()

    elif menu == "0":
        print("\nFinalizando...")
        break

    else:
        print("\nOpção inválida! Tente novamente.")



