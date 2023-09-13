import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

class JanelaEdicaoGanho:
    def __init__(self, master, item_id, ganho_mensal, ganho_adicional, descricao, salvar_callback):
        self._master = master
        self._item_id = item_id
        self._ganho_mensal = tk.StringVar(value=ganho_mensal)
        self._ganho_adicional = tk.StringVar(value=ganho_adicional)
        self._descricao = tk.StringVar(value=descricao)
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
        text_descricao = tk.Text(self._janela_edicao, height=4, width=30)
        text_descricao.insert("1.0", descricao)
        text_descricao.pack()

        ttk.Button(self._janela_edicao, text="Salvar", command=self.salvar).pack()

    def salvar(self):
        novo_ganho_mensal = self._ganho_mensal.get()
        novo_ganho_adicional = self._ganho_adicional.get()
        nova_descricao = self._descricao.get()

        self._salvar_callback(self._item_id, novo_ganho_mensal, novo_ganho_adicional, nova_descricao)

        self._janela_edicao.destroy()
