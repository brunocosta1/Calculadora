import os

def menu():
    opc = 0
    while (opc != 1 and opc != 2 and opc != 3):
        print("---------------SUDOKU-SOLVER------------------")
        print("")

        print("Menu de opções:\n")
        print("1 - Entrada dos valores por áudio.\n")
        print("2 - Entrada dos valors pelo teclado.\n")
        print("3 - Sair do programa.\n")

        opc = int(input())

        if not(opc == 1 or opc == 2 or opc == 3):
            print("Opção inválida, tente novamente.")
            os.system("sleep 2")
            os.system("clear")

    if(opc == 3):
        exit()

    return opc
