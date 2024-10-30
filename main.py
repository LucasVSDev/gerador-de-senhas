from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import string
import random

# Cores
COR_PRETO = "#444466"
COR_BRANCO = "#fafcff"
COR_AZUL = "#6f9fbd"
COR_VERMELHO = "#f05a43"
COR_CINZA_ESC = "#484f60"
FUNDO = COR_BRANCO

# Componentes para senha
ALFA_MAIOR = string.ascii_uppercase
ALFA_MENOR = string.ascii_lowercase
NUMERO = "1234567890"
SIMBOLOS = "[]{}()*;/,_-"


class GeradorDeSenhasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Senhas")
        self.root.configure(bg=FUNDO)
        self.root.resizable(width=False, height=False)
        self.configurar_janela()
        self.criar_frames()
        self.criar_widgets()

    def configurar_janela(self):
        largura_janela, altura_janela = 295, 360
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x = (largura_tela // 2) - (largura_janela // 2)
        y = (altura_tela // 2) - (altura_janela // 4)
        self.root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
        estilo = ttk.Style(self.root)
        estilo.theme_use("classic")

    def criar_frames(self):
        self.frame_cima = Frame(self.root, width=280, height=50, bg=COR_BRANCO, relief=FLAT)
        self.frame_cima.grid(row=0, column=0, sticky=NSEW)
        
        self.frame_baixo = Frame(self.root, width=295, height=310, bg=COR_PRETO, relief=FLAT)
        self.frame_baixo.grid(row=1, column=0, sticky=NSEW)

        self.frame_caracteres = Frame(self.frame_baixo, width=295, height=210, bg=COR_PRETO, relief=FLAT)
        self.frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

    def criar_widgets(self):
        self.carregar_imagem_logo()
        self.criar_labels_informacao()
        self.criar_controles_geracao()
        self.criar_botao_gerar_senha()

    def carregar_imagem_logo(self):
        img = Image.open("img/senha.png").resize((30, 30), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(img)
        Label(self.frame_cima, image=self.logo_img, bg=COR_BRANCO).place(x=3, y=0)
        Label(self.frame_cima, text="GERADOR DE SENHAS", font=("roboto 16 bold"), bg=COR_BRANCO, fg=COR_PRETO).place(x=35, y=2)

    def criar_labels_informacao(self):
        self.label_senha = Label(self.frame_baixo, text="- - -", width=25, height=2, font=("roboto 10 bold"), bg=COR_BRANCO, fg=COR_CINZA_ESC)
        self.label_senha.grid(row=0, column=0, sticky=NW, padx=3, pady=10)

        Label(self.frame_baixo, text="Total de caracteres na senha", font=("roboto 10 bold"), bg=COR_PRETO, fg=COR_BRANCO).grid(row=1, column=0, padx=5, pady=1)

        self.spin_valor = IntVar(value=8)
        self.spinbox = Spinbox(self.frame_baixo, from_=0, to=20, width=5, textvariable=self.spin_valor)
        self.spinbox.grid(row=2, column=0, sticky=NW, padx=5, pady=8)

    def criar_controles_geracao(self):
        self.estado_1 = StringVar(value=False)
        self.estado_2 = StringVar(value=False)
        self.estado_3 = StringVar(value=False)
        self.estado_4 = StringVar(value=False)

        self.criar_checkbutton("ABC Letras maiusculas", self.estado_1, ALFA_MAIOR, 0)
        self.criar_checkbutton("abc Letras minusculas", self.estado_2, ALFA_MENOR, 1)
        self.criar_checkbutton("123 Números", self.estado_3, NUMERO, 2)
        self.criar_checkbutton("Simbolos", self.estado_4, SIMBOLOS, 3)

    def criar_checkbutton(self, texto, var, valor, linha):
        Checkbutton(self.frame_caracteres, width=1, var=var, onvalue=valor, offvalue="off", bg=COR_PRETO).grid(row=linha, column=0, padx=2, pady=5)
        Label(self.frame_caracteres, text=texto, font=("roboto 10 bold"), bg=COR_PRETO, fg=COR_BRANCO).grid(row=linha, column=1, sticky=NW, padx=2, pady=5)

    def criar_botao_gerar_senha(self):
        Button(self.frame_caracteres, text="Gerar Senha", width=34, font=("roboto 10 bold"), bg=COR_AZUL, fg=COR_BRANCO, command=self.criar_senha).grid(row=5, column=0, padx=8, pady=15, columnspan=5)

    def criar_senha(self):
        combinar = ""
        if self.estado_1.get() == ALFA_MAIOR:
            combinar += ALFA_MAIOR
        if self.estado_2.get() == ALFA_MENOR:
            combinar += ALFA_MENOR
        if self.estado_3.get() == NUMERO:
            combinar += NUMERO
        if self.estado_4.get() == SIMBOLOS:
            combinar += SIMBOLOS

        comprimento = self.spin_valor.get()
        senha = "".join(random.sample(combinar, comprimento))
        self.label_senha.config(text=senha)

        self.criar_botao_copiar(senha)

    def criar_botao_copiar(self, senha):
        def copiar_para_clipboard():
            self.frame_baixo.clipboard_clear()
            self.frame_baixo.clipboard_append(senha)
            messagebox.showinfo("Sucesso", "A senha foi copiada")

        Button(self.frame_baixo, text="Copiar", width=7, font=("roboto 10 bold"), bg=COR_AZUL, fg=COR_BRANCO, command=copiar_para_clipboard).grid(row=0, column=1, padx=5, pady=7)


if __name__ == "__main__":
    root = Tk()
    app = GeradorDeSenhasApp(root)
    root.mainloop()
