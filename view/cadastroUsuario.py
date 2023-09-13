import re
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import sys

sys.path.insert(0, './')
sys.path.insert(0, './controller')
sys.path.insert(0, './models')

from controller.usuario import Usuario
from models.conexao import Conexao

class Cadastro:
    
    def validar_email(self, email):
        # Use uma expressão regular para verificar o formato do email
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
        if re.match(regex, email):
            return True
        else:
            return False
    
    def verifica_email(self, email):
        res = Conexao.retornar_usuario(f"SELECT * FROM usuarios WHERE email = '{email}';")
        if res:
            return True
        else:
            return False
        
    def cadastrar_usuario(self):
        nome = self._etr_nome.get()
        email = self._etr_email.get()
        senha = self._etr_senha.get()
        
        if nome and email and senha:

            if self.validar_email(email):
                if not self.verifica_email(email):
                    novo_usuario = Usuario(nome, email, senha)
                    messagebox.showinfo('Info', 'Seu usuário foi criado com sucesso')
                    self.voltar()
                else:
                    messagebox.showerror('Atenção', 'Email já cadastrado')
            else:
                messagebox.showerror('Atenção', 'Email em formato inválido')
        else:
            messagebox.showerror('Atenção', 'Preencha todos os campos')
        
    # def voltar(self):
    #     self._janela.destroy()
    #         novo_usuario = Usuario(nome, email, senha)
    #         messagebox.showinfo('Info', "Seu usuário foi criado com sucesso")
    #         self.voltar()
    #     else:
    #         messagebox.showerror("Atenção", "Preencha todos os campos!!")

    def voltar(self):
        self._janela.destroy()


    def __init__(self, master, photo):
        self._janela = master
        self._janela.title('Gestão Fácil/Cadastro')
        self._janela.geometry('800x500')
        self._photo = photo

        self._parte_verde = tk.Label(self._janela, background='#33bc7d')

        image = Image.open(r"logo (4).png")
        photo = ImageTk.PhotoImage(image)
        self._image_label = tk.Label(self._parte_verde, image=photo, bg='#33bc7d', width=450)
        self._image_label.image = photo  # Mantenha a referência à imagem
        self._image_label.pack()

        self._parte_verde.grid(row=0, column=0, rowspan=4, sticky="w")

        self._frame_cadastro = ttk.Frame(self._janela)
        self._frame_cadastro.grid(row=0, column=1)
        self._lbl_logo = ttk.Label(self._frame_cadastro, text='Cadastre-se')
        self._lbl_logo.config(font="Arial 15 bold")
        self._lbl_logo.grid(row=0, column=2, columnspan=4, pady=30)

        self._lbl_titulo = ttk.Label(self._frame_cadastro, text='Faça seu cadastro', font='Helvetica 10 bold')
        self._lbl_titulo.grid(row=0, column=3, pady=10, sticky="n")

        self._lbl_nome = ttk.Label(self._frame_cadastro, text='Nome:', width=30).grid(row=1, column=3, sticky="e")
        self._etr_nome = ttk.Entry(self._frame_cadastro, width=30)
        self._etr_nome.grid(row=2, column=3, sticky="e")

        self._lbl_email = ttk.Label(self._frame_cadastro, text='Email:', width=30).grid(row=3, column=3, sticky="e")
        self._etr_email = ttk.Entry(self._frame_cadastro, width=30)
        self._etr_email.grid(row=4, column=3, sticky="e")

        self._lbl_senha = ttk.Label(self._frame_cadastro, text='Senha:', width=30).grid(row=5, column=3, sticky="e")
        self._etr_senha = ttk.Entry(self._frame_cadastro, width=30)
        self._etr_senha.grid(row=6, column=3, sticky="e")

        self._btn_cadastrar = ttk.Button(self._frame_cadastro, text='Cadastrar', width=20, bootstyle="success-outline", command=self.cadastrar_usuario)
        self._btn_cadastrar.grid(row=7, column=3, pady=10)

        self._btn_voltar = ttk.Button(self._frame_cadastro, text='Voltar', width=15, bootstyle="success-outline", command=self.voltar)
        self._btn_voltar.grid(row=8, column=3, pady=10)

        # Configuração das colunas e linhas do grid
        self._janela.grid_columnconfigure(0, weight=1)
        self._janela.grid_columnconfigure(1, weight=1)
        self._janela.grid_rowconfigure(0, weight=1)
        self._janela.grid_rowconfigure(1, weight=1)
        self._janela.grid_rowconfigure(2, weight=1)
        self._janela.grid_rowconfigure(3, weight=1)

        self._janela.mainloop()


