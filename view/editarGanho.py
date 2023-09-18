import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from controller.registrarGanho import RegistrarGanho

class JanelaEdicaoGanho:
    def __init__(self, master, id_usuario, item_id, ganho_mensal, ganho_adicional, descricao, data_ganho, salvar_callback):
        self._master = master
        self._item_id = item_id
        self._usuario = id_usuario
        self._ganho_mensal = tk.StringVar(value=ganho_mensal)
        self._ganho_adicional = tk.StringVar(value=ganho_adicional)
        self._descricao = descricao
        self._data_ganho = data_ganho
        self._salvar_callback = salvar_callback

        self._janela_edicao = tk.Toplevel(master)
        self._janela_edicao.title("Editar Ganho")

        ttk.Label(self._janela_edicao, text="Ganho Mensal:").pack()
        entry_ganho_mensal = ttk.Entry(self._janela_edicao, textvariable=self._ganho_mensal)
        entry_ganho_mensal.pack()

        ttk.Label(self._janela_edicao, text="Ganho Adicional:").pack()
        entry_ganho_adicional = ttk.Entry(self._janela_edicao, textvariable=self._ganho_adicional)
        entry_ganho_adicional.pack()

        ttk.Label(self._janela_edicao, text="Descrição:").pack()
        self._text_descricao = tk.Text(self._janela_edicao, height=4, width=30)
        self._text_descricao.insert("1.0", descricao)
        self._text_descricao.pack()

        label_data = ttk.Label(self._janela_edicao, text='Data do Ganho:')
        label_data.pack()

        self._entry_data = ttk.Entry(self._janela_edicao)
        self._entry_data.insert(0, self._data_ganho)
        self._entry_data.pack()

        ttk.Button(self._janela_edicao, text="Salvar",  bootstyle="success-outline", command=self.salvar).pack()

    def salvar(self):
        novo_ganho_mensal = self._ganho_mensal.get()
        novo_ganho_adicional = self._ganho_adicional.get()
        nova_descricao = self._text_descricao.get("1.0", "end-1c")  # Obtém o texto do widget de texto
        nova_data = self._entry_data.get()
        
        RegistrarGanho.atualizar(self._usuario, novo_ganho_mensal, novo_ganho_adicional, nova_descricao, nova_data)

        self._salvar_callback(self._item_id, novo_ganho_mensal, novo_ganho_adicional, nova_descricao, nova_data)

        self._janela_edicao.destroy()
