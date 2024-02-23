import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random

def carregar_imagens():
    pasta = "imagens/"
    imagens = []
    for arquivo in os.listdir(pasta):
        caminho_completo = os.path.join(pasta, arquivo)
        img = Image.open(caminho_completo)
        img = img.resize((100, 100))
        imagem = ImageTk.PhotoImage(img)
        imagens.append(imagem)
    return imagens

def mostrarImagem(botao, indice):
    global imagens, jogada, indices, turno, vezJogar, pontos1, pontos2, listaBotoes
    botoes.append(botao)
    indices.append(indice)
    botao.config(bd=0, image=imagens[indice], width=100, height=100)
    jogada += 1
    if jogada == 2:
        jogada = 0

        if imagens[indices[0]] == imagens[indices[1]]:
            botoes.clear()
            indices.clear()
            if turno == 1:
                pontuacao[0] += 1
                pontos1.config(text=pontuacao[0])
            else:
                pontuacao[1] += 1
                pontos2.config(text=pontuacao[1])
            verificarVencedor()
        else:
            if turno == 1:
                turno = 0
            else:
                turno = 1

            for btn, cont in zip(listaBotoes, range(0, 18)):
                if indices[0] == cont or indices[1] == cont:
                    btn.config(state="normal")
                else:
                    btn.config(state="disabled")

            janela.after(1000, restaurarImagem)


def restaurarImagem():
    global botoes, img, indices, pontuacao, listaBotoes
    for btn in listaBotoes:
        btn.config(state="normal")
    indices.clear()
    botoes[0].config(image=img)
    botoes[1].config(image=img)
    botoes.clear()
    vezJogar.config(text="Jogador 1" if turno == 1 else "Jogador 2")

def verificarVencedor():
    global pontuacao
    if pontuacao[0] + pontuacao[1] == 9:
        if pontuacao[0] > pontuacao[1]:
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")

def resetar():
    global valor, jogada, botoes, indices, turno, pontuacao, imagens, pontos1, pontos2, vezJogar
    vezJogar.config(text="Jogador 1")
    pontos1.config(text="0")
    pontos2.config(text="0")
    valor = -1
    jogada = 0
    botoes = []
    indices = []
    turno = 1
    pontuacao = [0, 0]
    random.shuffle(imagens)
    for i in range(3):
        for j in range(6):
            valor += 1
            button = tk.Button(janela)
            button.place(x=20 + j * 110, y=10 + i * 110)
            button.config(image=img, width=100, height=100, text=valor + 1,
                          command=lambda v=valor, btn=button: mostrarImagem(btn, v))


janela = tk.Tk()
janela.title("Jogo da Memoria")
janela.geometry("700x400")

imagens = carregar_imagens()
imagens = imagens * 2
random.shuffle(imagens)

valor = -1
jogada = 0
botoes = []
indices = []
turno = 1
pontuacao = [0,0]
listaBotoes = []

img = Image.open("capa.png")
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)

for i in range(3):
    for j in range(6):
        valor += 1
        button = tk.Button(janela)
        button.place(x=20 + j * 110, y=10 + i * 110)
        button.config(image=img, width=100, height=100, text=valor+1, command=lambda v=valor, btn=button: mostrarImagem(btn, v))
        listaBotoes.append(button)

reset = tk.Button(janela, text="Resetar", command=resetar)
reset.place(x=600, y=350)

label = tk.Label(janela, text="Vez de jogar:")
label.place(x=20, y=350)
vezJogar = tk.Label(janela, text="Jogador 1" if turno == 1 else "Jogador 2")
vezJogar.place(x=100, y=350)

label1 = tk.Label(janela, text="Jogador 1:")
label1.place(x=300, y=350)
pontos1 = tk.Label(janela, text="0")
pontos1.place(x=360, y=350)

label2 = tk.Label(janela, text="Jogador 2:")
label2.place(x=450, y=350)
pontos2 = tk.Label(janela, text="0")
pontos2.place(x=510, y=350)

janela.mainloop()
