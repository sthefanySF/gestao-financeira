import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import webbrowser

import sys




sys.path.insert(0, './')
sys.path.insert(0, './controller')
sys.path.insert(0, './view')
from view.recuperarSenha import RecuperarSenha
from telaInicial import TelaInicial
from cadastroUsuario import Cadastro
from perfilUsuario import PerfilUsuario
from controller.usuario import Usuario




    

class Login:
    
   
    # def entrar(self):
    #     tela_inicial_toplevel = tk.Toplevel(self._janela)
    #     tela_inicial = TelaInicial(tela_inicial_toplevel)
    def entrar(self):
        email = self._etr_email.get()
        senha = self._etr_senha.get()

        usuario_autenticado = Usuario.autenticar(email, senha)

        if usuario_autenticado:
            # Esconda a janela de login
            self._janela.withdraw()

            tela_inicial_toplevel = tk.Toplevel(self._janela)
            tela_inicial = TelaInicial(tela_inicial_toplevel, usuario_autenticado, self)
        else:
            messagebox.showwarning('Atenção', 'Email ou senha inválidos!')

    def mostrar_login(self):
        # Mostrar a janela de login novamente
        self._janela.deiconify()

    def mostrar(self,event):
        if self._senha_oculta:
            self._senha_var.set(self._etr_senha.get())
            self._etr_senha.config(show='')
        else:
            self._etr_senha.config(show='*')
        self._senha_oculta = not self._senha_oculta 

        
    def abrir_cadastrar(self):
       recuperar = tk.Toplevel(self._janela)
       janela = Cadastro(recuperar,self._photo)
    
    def abrir_janela_recuperacao_senha(self,event):
       recuperar = tk.Toplevel(self._janela)
       recuperar_senha = RecuperarSenha(recuperar)

    
    
    def __init__(self, master):
        self._janela = master
        self._janela.title('Gestão Fácil/Login')
        self._janela.geometry('800x500')
        # Variável de instância para controlar o estado da janela de login
        self._login_window_visible = True

        self._parte_verde = tk.Label(self._janela, background='#33bc7d')

        image = Image.open(r"logo (4).png")
        self._photo = ImageTk.PhotoImage(image)
        self._image_label = tk.Label(self._parte_verde, image=self._photo, bg='#33bc7d', width=450)
        self._image_label.image = self._photo
        self._image_label.pack()

        self._parte_verde.grid(row=0, column=0, rowspan=4, sticky="w")

        self._frame_login = ttk.Frame(self._janela)
        self._frame_login.grid(row=0, column=1)

        self._lbl_logo = ttk.Label(self._frame_login, text='Entre ou crie sua conta')
        self._lbl_logo.config(font="Arial 12 bold")
        self._lbl_logo.grid(row=0, column=2, columnspan=4, pady=50)

        self._lbl_email = ttk.Label(self._frame_login, text='Email:', width=30).grid(row=1, column=3, sticky="e")
        self._etr_email = ttk.Entry(self._frame_login, width=30)
        self._etr_email.grid(row=2, column=3, sticky="e")

        self._senha_var = tk.StringVar()
        self._lbl_senha = ttk.Label(self._frame_login, text='Senha:', width=30).grid(row=3, column=3, sticky="e")
        self._etr_senha = ttk.Entry(self._frame_login, width=30,show="*",textvariable=self._senha_var)
        self._etr_senha.grid(row=4, column=3, sticky="e")
        
        self._ver_label = ttk.Label(self._frame_login, text="◉", cursor="hand2", font=("Arial", 12))
        self._ver_label.grid(row=4, column=4, pady=10)          
        self._ver_label.bind("<Button-1>", self.mostrar)
        self._senha_oculta = True

        self._link_label = ttk.Label(self._frame_login, text="esqueci a senha", cursor="hand2", font=("Helvetica", 8, "underline"))

        self._link_label.grid(row=5, column=3, sticky="e")  # Centraliza na coluna da direita
        self._link_label.bind("<Button-1>",self.abrir_janela_recuperacao_senha)


        self._btn = ttk.Button(self._frame_login, text='Entrar', width=20, bootstyle="success", command=self.entrar)
        self._btn.grid(row=6, column=3, pady=10)

        self._btn_cadastrar = ttk.Button(self._frame_login, text='Cadastar', bootstyle="success-outline", command=self.abrir_cadastrar)
        self._btn_cadastrar.grid(row=7, column=3, pady=10)

        # Configuração das colunas e linhas do grid
        self._janela.grid_columnconfigure(0, weight=1)
        self._janela.grid_columnconfigure(1, weight=1)
        self._janela.grid_rowconfigure(0, weight=1)
        self._janela.grid_rowconfigure(1, weight=1)
        self._janela.grid_rowconfigure(2, weight=1)
        self._janela.grid_rowconfigure(3, weight=1)

        self._janela.mainloop()

if __name__ == "__main__":
    root = ttk.Window(themename='litera')
    login = Login(root)
    root.mainloop()
