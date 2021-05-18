# Arquivo responsável para a entrada dos valores do sudoku.

import speech_recognition as sr
import os
import numpy as np

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def ouvir_microfone():

    lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source)

            try:
                frase = microfone.recognize_google(audio, language='pt-BR')
                if frase in lista:
                    print("Você disse: "+ frase)
                    break
                else:
                    print("O que você disse não é um número de 1 a 9. Repita.")
            except sr.UnknownValueError:
                print("Não entendi.")

    return frase

def InputValues():
    global grid

    for i in range(9):
        for j in range(9):
            print(np.matrix(grid))
            print("Fale o valor que se encontra na linha "+str(i)+"coluna"+str(j)+":")
            grid[i][j] = int(ouvir_microfone())
            print(np.matrix(grid))
            os.system("sleep 0.5")
            os.system("clear")

