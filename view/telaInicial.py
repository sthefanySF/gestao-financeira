import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import webbrowser
import sys

sys.path.insert(0, './')
sys.path.insert(0, './controller')

from controller.reegistrarGasto import RegistrarGasto
from controller.registrarGanho import RegistrarGanho

from perfilUsuario import PerfilUsuario
from registrarTransacao import RegistrarTransacoes
from extratos import Extratos
#from extratos import Extratos




class TelaInicial:
    def __init__(self,master,usuario, login_window=None):
        self._id_usuario_atual = usuario
        self._janela = master
        self._janela.title('Gestão Fácil/Tela inicial')
        self._janela.geometry('850x500')
        from loginUsuario import Login
        self._login_window = login_window  # Mantenha a referência à janela de login

        frame_menu = ttk.Frame(self._janela)
        frame_menu.grid(row=0, column=0)
        margin_menu = 10 

        self._btn_perfil = ttk.Button(frame_menu, text='Meu perfil', width=20, bootstyle="success", command=self.abrir_perfil)
        self._btn_perfil.grid(row=0, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_inicio = ttk.Button(frame_menu, text='Inicio', width=20, bootstyle="success")
        self._btn_inicio.grid(row=1, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_regis = ttk.Button(frame_menu, text='Registrar Transação', width=20, bootstyle="success", command=self.abrir_transacoes)
        self._btn_regis.grid(row=2, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_extrato = ttk.Button(frame_menu, text='Extrato', width=20, bootstyle="success", command=self.abrir_extratro)
        self._btn_extrato.grid(row=3, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_voltar = ttk.Button(frame_menu, text='Voltar', width=20, bootstyle="success", command=self.voltar)
        self._btn_voltar.grid(row=5, column=0, sticky='w', pady=margin_menu, padx=margin_menu)


        
        frame_resumo_mes = ttk.LabelFrame(self._janela, text="Resumo do Mês", padding=(10, 10))
        frame_resumo_mes.grid(row=0, column=2, rowspan=5, columnspan=2, padx=10, pady=margin_menu)

        self._mtr1 = ttk.Meter(frame_resumo_mes, subtext='Saldo', bootstyle='success', interactive=False, amountused=self.saldo())
        self._mtr1.grid(row=0, column=0, sticky='e', padx=10, pady=10)

        self._mtr2 = ttk.Meter(frame_resumo_mes, subtext='Gastos', bootstyle='danger', interactive=False, amountused=self.gastos())
        self._mtr2.grid(row=0, column=1, sticky='e', padx=10, pady=10)

        
        # self._lbl_meter = ttk.Label(self._janela, text='Resumo do mês')
        # self._lbl_meter.grid(row=0, column=2, columnspan=2, pady=(margin_menu * 2, 0))
        # self._lbl_meter.config(font="Arial 13 bold")
    def mostrar_tela_inicial(self):
        self._janela.deiconify()  # Reexibe a janela da tela inicial

    def abrir_perfil(self):
        # Esconda a janela de TelaInicial
        self._janela.withdraw()

        perfil_window = PerfilUsuario(self._janela, self._id_usuario_atual, self._login_window,self)
    
    def abrir_extratro(self):
        self._janela.withdraw()
        self._janela_Extrato = tk.Toplevel(self._janela)

        extrato_window = Extratos(self._janela_Extrato,self._id_usuario_atual)
        
    
    def abrir_transacoes(self):
        self._janela.withdraw()
        self._janela_transacoes = tk.Toplevel(self._janela)
        transacao = RegistrarTransacoes(self._janela_transacoes, self._id_usuario_atual)
        
    def voltar(self):
        self._janela.destroy()
        
    def saldo(self):
        ganho = RegistrarGanho.ganho_total(self._id_usuario_atual)
        gasto = RegistrarGasto.retornar_total_gastos(self._id_usuario_atual)

        if  ganho[0] != (None,):
            
           saldo = float(ganho[0][0])
            
        elif  ganho[0] == (None,) or gasto[0] == (None,):
            
            saldo = 0
            
        else:
            saldo = float(ganho[0][0]) - float(gasto[0][0])

        return saldo

    def gastos(self):
        gasto = RegistrarGasto.retornar_total_gastos(self._id_usuario_atual)

        if gasto[0] == (None,):
            gasto_total = 0
        else:
            gasto_total = float(gasto[0][0])

        return gasto_total
