import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import webbrowser

from perfilUsuario import PerfilUsuario
from registrarTransacao import RegistrarTransacoes
from extratos import Extratos

class TelaInicial:
    def __init__(self,master,usuario):
        self._id_usuario_atual = usuario
        self._janela = master
        self._janela.title('Gestão Fácil/Tela inicial')
        self._janela.geometry('850x500')

        frame_menu = ttk.Frame(self._janela)
        frame_menu.grid(row=0, column=0)
        margin_menu = 3
        self._btn_perfil = ttk.Button(frame_menu, text='Meu perfil', width=20, bootstyle="success", command=self.abrir_perfil)
        self._btn_perfil.grid(row=0, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_inicio = ttk.Button(frame_menu, text='Inicio', width=20, bootstyle="success")
        self._btn_inicio.grid(row=1, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_regis = ttk.Button(frame_menu, text='Registrar Transação', width=20, bootstyle="success", command=self.abrir_transacoes)
        self._btn_regis.grid(row=2, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_extrato = ttk.Button(frame_menu, text='Extrato', width=20, bootstyle="success",command= self.abrir_extratro)
        self._btn_extrato.grid(row=3, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_contas = ttk.Button(frame_menu, text='Minhas contas', width=20, bootstyle="success")
        self._btn_contas.grid(row=4, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_voltar = ttk.Button(frame_menu, text='Voltar', width=20, bootstyle="success", command=self.voltar)
        self._btn_voltar.grid(row=5, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._lbl_meter = ttk.Label(self._janela, text='Resumo do mês')
        self._lbl_meter.grid(row=0, column=4, columnspan=2)
        self._lbl_meter.config(font="Arial 13 bold")

        self._mtr1 = ttk.Meter(self._janela, subtext='Saldo', bootstyle='success', interactive=False, amountused=50)
        self._mtr1.grid(row=1, column=4, rowspan=4, sticky='e', padx=20)

        self._mtr2 = ttk.Meter(self._janela, subtext='Gastos', bootstyle='danger', interactive=False, amountused=20)
        self._mtr2.grid(row=1, column=5, rowspan=4, sticky='e', padx=20)
        
        
    def abrir_perfil(self):
        perfil_window = PerfilUsuario(self._janela)
    def abrir_extratro(self):
        extrato_window = Extratos(self._janela,self._id_usuario_atual)
        
    
    def abrir_transacoes(self):
        self._janela_transacoes = tk.Toplevel(self._janela)
        transacao = RegistrarTransacoes(self._janela_transacoes, self._id_usuario_atual)
        
    def voltar(self):
        self._janela.destroy()

        
