from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

import string
import random

# cores
# cor1 = "#0a0a0a"  # black / preta
# cor2 = "#fafcff"  # white / branca
# cor3 = "#21c25c"  # green / verde
# cor4 = "#eb463b"  # red / vermelha
# cor5 = "#dedcdc"  # gray / Cizenta
# cor6 = "#3080f0"  # blue / azul

# Cores -------------------
cor0 = "#444466"  # preta / black
cor1 = "#feffff"  # branco / white
cor2 = "#f05a43"  # vermehlo / red

janela = Tk()
window_height = 350
window_width = 295

screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (screen_height / 4))

janela.title("")
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)
janela.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

stylo = ttk.Style(janela)
stylo.theme_use("clam")

############## Configuração frames ###################
frame_cima = Frame(janela, width=280, height=50, bg=cor1, padx=0, pady=0, relief=FLAT)
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor0, padx=0, pady=0, relief=FLAT)
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Trabalhando frame cima ----------------------------------
img = Image.open(r"img/senha.png")
img = img.resize((30, 30), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)

app_logo = Label(
    frame_cima,
    height=60,
    image=img,
    compound=LEFT,
    padx=10,
    relief="flat",
    anchor="nw",
    bg=cor1,
)
app_logo.place(x=3, y=0)

app_logo = Label(
    frame_cima,
    text="GERADOR DE SENHAS",
    width=20,
    height=1,
    padx=0,
    relief="flat",
    anchor="nw",
    font=("roboto 16 bold"),
    bg=cor1,
    fg=cor0,
)
app_logo.place(x=35, y=2)
# Trabalhando frame baixo ---------------------------------

app_senha = Label(
    frame_baixo,
    text=" - - -",
    width=26,
    height=2,
    padx=0,
    relief="solid",
    anchor="center",
    font=("roboto 10 bold"),
    bg=cor1,
    fg=cor0,
)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(
    frame_baixo,
    text="Total de caracteres na senha",
    height=1,
    padx=0,
    relief="flat",
    anchor="nw",
    font=("roboto 10 bold"),
    bg=cor0,
    fg=cor1,
)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

var = IntVar()
var.set(8)
spin = Spinbox(
    frame_baixo,
    from_=0,
    to=20,
    width=5,
    textvariable=var,
)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)

alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numero = "1234567890"
simbolos = "[]{}()*;/,_-"
# simbolos = "@&%$+?="

frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=cor0, padx=0, pady=0, relief=FLAT)
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

# ---------------------------- LETRAS MAIUSCULAS ------------------------------------
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=alfa_maior, offrelief="flat", offvalue="off", bg=cor0, fg=cor0)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
l_maior = Label(
    frame_caracteres,
    text="ABC Letras maiusculas",
    height=1,
    padx=0,
    relief="flat",
    anchor="nw",
    font=("roboto 10 bold"),
    bg=cor0,
    fg=cor1,
)
l_maior.grid(row=0, column=1, sticky=NW, padx=2, pady=5)

# ---------------------------- LETRAS MENUSCULAS ------------------------------------
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, onvalue=alfa_menor, offrelief="flat", offvalue="off", bg=cor0, fg=cor0)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
l_menor = Label(
    frame_caracteres,
    text="ABC Letras minusculas",
    height=1,
    padx=0,
    relief="flat",
    anchor="nw",
    font=("roboto 10 bold"),
    bg=cor0,
    fg=cor1,
)
l_menor.grid(row=1, column=1, sticky=NW, padx=2, pady=5)

# ---------------------------- NUMEROS ------------------------------------
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, onvalue=numero, offrelief="flat", offvalue="off", bg=cor0, fg=cor0)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
l_numero = Label(
    frame_caracteres,
    text="123 Numeros",
    height=1,
    padx=0,
    relief="flat",
    anchor="nw",
    font=("roboto 10 bold"),
    bg=cor0,
    fg=cor1,
)
l_numero.grid(row=2, column=1, sticky=NW, padx=2, pady=5)

# ---------------------------- CARACTERIS ------------------------------------
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4, onvalue=simbolos, offrelief="flat", offvalue="off", bg=cor0, fg=cor0)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
l_caracteris = Label(
    frame_caracteres,
    text="Simblos",
    height=1,
    padx=0,
    relief="flat",
    anchor="nw",
    font=("roboto 10 bold"),
    bg=cor0,
    fg=cor1,
)
l_caracteris.grid(row=3, column=1, sticky=NW, padx=2, pady=5)

# ------------------------ BOTÃO GERA SENHA ---------------------------------------------
b_botao_senha= Button(
    frame_caracteres,
    text="Gerar Senha",
    width=34,
    height=1,
    relief="flat",
    overrelief="solid",
    anchor="center",
    font=("roboto 10 bold"),
    bg=cor2,
    fg=cor1,
)
b_botao_senha.grid(row=5, column=0, sticky=NSEW, padx=8, pady=5, columnspan=5)

# ------------------------ BOTÃO COPIA ---------------------------------------------
b_botao_copia= Button(
    frame_baixo,
    text="Copiar",
    width=7,
    height=2,
    relief="ridge",
    overrelief="solid",
    anchor="center",
    font=("roboto 10 bold"),
    bg=cor2,
    fg=cor1,
)
b_botao_copia.grid(row=0, column=1, sticky=NW, padx=5, pady=10, columnspan=1)

janela.mainloop()
