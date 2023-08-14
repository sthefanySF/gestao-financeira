import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import webbrowser

from telaInicial import TelaInicial

def open_link(event):
    webbrowser.open("https://www.example.com")  # Substitua pelo link real

class Login:
   
    def entrar(self):
        tela = TelaInicial(self._janela)  # Cria uma instância da classe Tela


    def __init__(self):
        self._janela = ttk.Window(themename='litera')
        self._janela.geometry('800x500')
        self._janela.title('Gestão Fácil/Login')

        self._parte_verde = tk.Label(self._janela, background='#33bc7d')

        image = Image.open(r"C:\Users\sthef\OneDrive\Documentos\GitHub\gestao-financeira\logo (4).png")  # Substitua pelo caminho real da imagem
        photo = ImageTk.PhotoImage(image)
        self._image_label = tk.Label(self._parte_verde, image=photo, bg='#33bc7d', width=450)
        self._image_label.pack()

        self._parte_verde.grid(row=0, column=0, rowspan=4, sticky="w")

        self._frame_login = ttk.Frame(self._janela)
        self._frame_login.grid(row=0, column=1)

        self._lbl_logo = ttk.Label(self._frame_login, text='Entre ou crie sua conta')
        self._lbl_logo.config(font="Arial 10 bold")
        self._lbl_logo.grid(row=0, column=2, columnspan=4, pady=50)

        self._lbl_email = ttk.Label(self._frame_login, text='Email:', width=30).grid(row=1, column=3, sticky="e")
        self._etr_email = ttk.Entry(self._frame_login, width=30).grid(row=2, column=3, sticky="e")

        self._lbl_senha = ttk.Label(self._frame_login, text='Senha:', width=30).grid(row=3, column=3, sticky="e")
        self._etr_senha = ttk.Entry(self._frame_login, width=30).grid(row=4, column=3, sticky="e")

        self._link_label = ttk.Label(self._frame_login, text="esqueci a senha", cursor="hand2", font=("Helvetica", 8, "underline"))
        self._link_label.grid(row=5, column=3, sticky="e")  # Centraliza na coluna da direita
        self._link_label.bind("<Button-1>", open_link)

        self._btn = ttk.Button(self._frame_login, text='Entrar', width=20, bootstyle="success", command=self.entrar)
        self._btn.grid(row=6, column=3, pady=10)

        self._btn_cadastrar = ttk.Button(self._frame_login, text='Cadastar', bootstyle="success-outline").grid(row=7, column=3, pady=10)

        # Configuração das colunas e linhas do grid
        self._janela.grid_columnconfigure(0, weight=1)
        self._janela.grid_columnconfigure(1, weight=1)
        self._janela.grid_rowconfigure(0, weight=1)
        self._janela.grid_rowconfigure(1, weight=1)
        self._janela.grid_rowconfigure(2, weight=1)
        self._janela.grid_rowconfigure(3, weight=1)

        self._janela.mainloop()

if __name__ == "__main__":
    login = Login()
