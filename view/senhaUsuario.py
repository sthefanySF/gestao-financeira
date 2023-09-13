import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from conexao import Conexao
from controller import usuario

class SenhaUsuario:
    def __init__(self, master, id_usuario_logado):
        self._janela = master
        self._janela.title('Gestão Fácil/Senha do Usuário')
        self._janela.geometry('800x500')
        self.usuario = id_usuario_logado

        self.frame_senha = ttk.Frame(self._janela)
        self.frame_senha.pack(expand=True)
        
        self._lbl_titulo = ttk.Label(self.frame_senha, text='Senha do Usuário', font='Helvetica 18 bold')
        self._lbl_titulo.grid(row=0, column=1, columnspan=3, pady=20)

        senha_label = ttk.Label(self.frame_senha, text="Senha:", width=20)
        senha_label.grid(row=1, column=1, padx=10, pady=5, columnspan=1)
        self.senha_entry = ttk.Entry(self.frame_senha, width=50, bootstyle="success-primary")
        self.senha_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky="w")

        self.preencher_senha()

        atualizar_botao = ttk.Button(self.frame_senha, text="Atualizar", command=self.atualizar_senha, width=15, bootstyle="success-outline")
        atualizar_botao.grid(row=3, column=1, pady=10, columnspan=4)

        voltar_botao = ttk.Button(self.frame_senha, text="Voltar", command=self.voltar, width=10, bootstyle="success-primary")
        voltar_botao.grid(row=4, column=1, pady=10, columnspan=4)

    def preencher_senha(self):
        sql = f'SELECT senha FROM usuarios WHERE id = {self.usuario};'
        senha = Conexao.retornar_usuario(sql)
        print(senha)
        self.senha_entry.insert(0, senha[0])

    def atualizar_senha(self):
        nova_senha = self.senha_entry.get()
        sql = f'''UPDATE usuarios SET senha = '{nova_senha}' WHERE id = {self.usuario};'''
        Conexao.atualizar(sql)
        messagebox.showinfo('Sucesso', 'Senha atualizada com sucesso!')

    def voltar(self):
        self._janela.destroy()  # Fecha a janela atual
