from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from controller.registrarGanho import RegistrarGanho

from perfilUsuario import PerfilUsuario
import sys



sys.path.insert(0, './')
sys.path.insert(0, './controller')


class RegistrarTransacoes:
    def __init__(self, master, id_usuario_atual):
        self._id_usuario_atual = id_usuario_atual
        self._janela = master
        self._janela.title('Gestão Fácil/Registrar transações')
        self._janela.geometry('850x500')

        self._frame_principal = ttk.Frame(self._janela)
        self._frame_principal.grid(row=0, column=0, sticky="nsew")
        self._janela.grid_rowconfigure(0, weight=1)
        self._janela.grid_columnconfigure(0, weight=1)

        frame_menu = ttk.Frame(self._frame_principal)
        frame_menu.grid(row=0, column=0, rowspan=2, sticky="ns")
        margin_menu = 10

        self._btn_perfil = ttk.Button(frame_menu, text='Meu perfil', width=20, bootstyle="success", command=self.abrir_perfil)
        self._btn_perfil.grid(row=0, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_inicio = ttk.Button(frame_menu, text='Inicio', width=20, bootstyle="success", command=self.entrar)
        self._btn_inicio.grid(row=1, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_regis = ttk.Button(frame_menu, text='Registrar Transação', width=20, bootstyle="success")
        self._btn_regis.grid(row=2, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_extrato = ttk.Button(frame_menu, text='Extrato', width=20, bootstyle="success", command=self.abrir_extratro)
        self._btn_extrato.grid(row=3, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_contas = ttk.Button(frame_menu, text='Minhas contas', width=20, bootstyle="success", command=self.abrir_perfil)
        self._btn_contas.grid(row=4, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_voltar = ttk.Button(frame_menu, text='Voltar', width=20, bootstyle="success", command=self.voltar)
        self._btn_voltar.grid(row=5, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        # LabelFrame de Registrar ganhos
        self._frame_ganhos = ttk.LabelFrame(self._frame_principal, text="Registrar ganhos")
        self._frame_ganhos.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self._frame_ganhos.grid_rowconfigure(0, weight=1)
        self._frame_ganhos.grid_columnconfigure(0, weight=1)

        ttk.Label(self._frame_ganhos, text="Ganho mensal:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self._entry_ganho_mensal = ttk.Entry(self._frame_ganhos)
        self._entry_ganho_mensal.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        
        ttk.Label(self._frame_ganhos, text="Ganho adicional:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self._entry_ganho_adicional = ttk.Entry(self._frame_ganhos)
        self._entry_ganho_adicional.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        
        ttk.Label(self._frame_ganhos, text="Descrição do ganho adicional:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self._text_descricao_ganhos = tk.Text(self._frame_ganhos, height=4, width=30)
        self._text_descricao_ganhos.grid(row=5, column=0, padx=10, pady=5, sticky="ew")
        
        ttk.Button(self._frame_ganhos, text="Registrar Ganho", bootstyle="success-outline",command=self.registar_ganho).grid(row=8, column=0, padx=10, pady=10, sticky="ew")

        # LabelFrame de Registrar gastos
        self._frame_gastos = ttk.LabelFrame(self._frame_principal, text="Registrar gastos")
        self._frame_gastos.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)
        self._frame_gastos.grid_rowconfigure(0, weight=1)
        self._frame_gastos.grid_columnconfigure(0, weight=1)

        ttk.Label(self._frame_gastos, text="Valor do gasto:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self._entry_valor = ttk.Entry(self._frame_gastos)
        self._entry_valor.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        ttk.Label(self._frame_gastos, text="Descrição:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self._text_descricao = tk.Text(self._frame_gastos, height=4, width=30)
        self._text_descricao.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        ttk.Label(self._frame_gastos, text="Categoria:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self._combo_categoria = ttk.Combobox(self._frame_gastos, values=["Alimentação", "Transporte", "Outros"])
        self._combo_categoria.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

        ttk.Label(self._frame_gastos, text="Data:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self._datepicker_data = ttk.DateEntry(self._frame_gastos)
        self._datepicker_data.grid(row=7, column=0, padx=10, pady=5, sticky="ew")

        ttk.Button(self._frame_gastos, text="Registrar Gasto",bootstyle="success-outline", command=self.registrar_gasto).grid(row=8, column=0, padx=10, pady=10, sticky="ew")
    
    def abrir_perfil(self):
        perfil_window = PerfilUsuario(self._janela,self._id_usuario_atual)
    
    def abrir_transacoes(self):
        self._janela_transacoes = tk.Toplevel(self._janela)
        transacao = RegistrarTransacoes(self._janela_transacoes, self._id_usuario_atual)
        
    def entrar(self):
        from telaInicial import TelaInicial
        tela_inicial_toplevel = tk.Toplevel(self._janela)
        tela_inicial = TelaInicial(tela_inicial_toplevel, self._id_usuario_atual)
        
    def abrir_extratro(self):
        from extratos import Extratos

        self._janela_Extrato = tk.Toplevel(self._janela)

        extrato_window = Extratos(self._janela_Extrato,self._id_usuario_atual)
        
        
    def voltar(self):
        self._janela.destroy()

    def registar_ganho(self):
        ganho_mensal = self._entry_ganho_mensal.get()
        ganho_adicional = self._entry_ganho_adicional.get()
        descricao = self._text_descricao_ganhos.get('1.0', 'end')
      
        novo_ganho = RegistrarGanho(self._id_usuario_atual,ganho_mensal,ganho_adicional,descricao)
        self.voltar
        return messagebox.showinfo("Registro de ganho","Ganho registrado com sucesso!")
    
    def registrar_gasto(self):
        pass
if __name__ == "__main__":
    root = ttk.Window()  # Escolha um tema do ttkbootstrap
    login = RegistrarTransacoes(root)
    root.mainloop()