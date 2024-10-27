#importes ##########################################
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import ImageTk, Image

import string
import random

### Cores #####################################################################
cor0 = "#444466" # preta
cor1 = "#fafcff" # branco
cor2 = "#6f9fbd" # azul
cor3 = "#f05a43" # vermehlo
letra_dark = "#484f60" #cinza escuro
fundo = cor1 
##################### Configuração da janela ##################################
janela = Tk()
janela.title("")
janela.configure(bg=fundo)
janela.resizable(width=FALSE, height=FALSE)
window_height = 360
window_width = 295

################## Fixa a janela no meio ######################################
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (screen_height / 4))

janela.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

stylo = ttk.Style(janela)
stylo.theme_use("classic")

###################### Configuração frames ####################################
frame_cima = Frame(janela, width=280, height=50, bg=cor1, padx=0, pady=0, relief=FLAT)
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor0, padx=0, pady=0, relief=FLAT)
frame_baixo.grid(row=1, column=0, sticky=NSEW)

######################## Trabalhando frames cima ###############################
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

############################### Funções #######################################
alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numero = "1234567890"
simbolos = "[]{}()*;/,_-"

def criar_senha():
    alfa_maior = string.ascii_uppercase
    alfa_menor = string.ascii_lowercase
    numero = "1234567890"
    simbolos = "[]{}()*;/,_-"
    
    global combinar
    
    # ---- condição para maiuscula
    if estado_1.get() == alfa_maior:
        combinar = alfa_maior
    else:
        ...
    # ---- condição para menuscula
    if estado_2.get() == alfa_menor:
        combinar = combinar + alfa_menor
    else:
        ...
    # ---- condição para numeros
    if estado_3.get() == numero:
        combinar = combinar + numero
    else:
        ...
    # ---- condição para simbolos
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        ...
        
    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento))
    
    app_senha["text"] = senha
    def copia_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)
        
        messagebox.showinfo("Sucesso", "A senha foi copiada")
        
        # ------------------------ BOTÃO COPIA ---------------------------------------------
    b_copia= Button(
            frame_baixo,
            command=copia_senha,
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
    b_copia.grid(row=0, column=1, sticky=NW, padx=5, pady=7, columnspan=1)

#################### Trabalhando frames baixo ##################################
app_senha = Label(
    frame_baixo,
    text="- - -",
    width=25,
    height=2,
    padx=0,
    relief="solid",
    anchor="center",
    font=("roboto 10 bold"),
    bg=cor1,
    fg=letra_dark,
)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NW, padx=3, pady=10)

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

frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=cor0, padx=0, pady=0, relief=FLAT)
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

# ---------------------------- LETRAS MAIUSCULAS ------------------------------
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

# ---------------------------- LETRAS MENUSCULAS ------------------------------
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

# ---------------------------- NUMEROS ----------------------------------------
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

# ---------------------------- CARACTERES -------------------------------------
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

# ------------------------ BOTÃO GERAR SENHA -----------------------------------
b_botao_senha= Button(
    frame_caracteres,
    command=criar_senha,
    text="Gerar Senha",
    width=34,
    height=1,
    relief="raised",
    overrelief="solid",
    anchor="center",
    font=("roboto 10 bold"),
    bg=cor2,
    fg=cor1,
)
b_botao_senha.grid(row=5, column=0, sticky=NSEW, padx=8, pady=15, columnspan=5)

janela.mainloop()