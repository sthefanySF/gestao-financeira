import tkinter as tk
import ttkbootstrap as ttk
import sys
from conexao import Conexao
sys.path.insert(0, './')
sys.path.insert(0, './controller')
from controller import usuario

class MeusDados:
    def __init__(self, master, id_usuario_logado):
        self._janela = master
        self.usuario = id_usuario_logado
        self._janela.title('Gestão Fácil/Dados do Usuário')
        self._janela.geometry('800x500')

        self.frame_dados = ttk.Frame(self._janela)
        self.frame_dados.pack(expand=True)
        
        self._lbl_nome_usuario = ttk.Label(self.frame_dados, text='Meus Dados', font='Helvetica 18 bold')
        self._lbl_nome_usuario.grid(row=0, column=1, columnspan=3, pady=20)

        nome_label = ttk.Label(self.frame_dados, text="Nome:", width=20)
        nome_label.grid(row=1, column=1, padx=10, pady=5, columnspan=1)
        self.nome_entry = ttk.Entry(self.frame_dados, width=50, bootstyle="success-primary")
        self.nome_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky="w")

        email_label = ttk.Label(self.frame_dados, text="E-mail:", width=20)
        email_label.grid(row=3, column=1, padx=10, pady=5, columnspan=1)
        self.email_entry = ttk.Entry(self.frame_dados, width=50, bootstyle="success-primary")
        self.email_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky="w")

        self.preencher_campos()

        atualizar_botao = ttk.Button(self.frame_dados, text="Atualizar", command=self.atualizar_informacoes, width=15, bootstyle="success-outline")
        atualizar_botao.grid(row=5, column=1, pady=10, columnspan=4)

        voltar_botao = ttk.Button(self.frame_dados, text="Voltar", command=self.voltar, width=10, bootstyle="success-primary")
        voltar_botao.grid(row=6, column=1, pady=10, columnspan=4)

    def preencher_campos(self):
        # Preencha os campos Entry com os dados do usuário
        self.nome_entry.insert(0, self.usuario._nome)  # Use _nome aqui
        self.email_entry.insert(0, self.usuario._email)

    def atualizar_informacoes(self):
        novo_nome = self.nome_entry.get()
        novo_email = self.email_entry.get()

        if novo_nome and novo_email:
            conexao = Conexao

            
    def voltar(self):
        self._janela.destroy()  # Fecha a janela atual

