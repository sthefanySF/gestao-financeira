import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from controller import usuario

from perfilUsuario import PerfilUsuario
from registrarTransacao import RegistrarTransacoes

class Extratos:
    def __init__(self, master):
        self._id_usuario_atual = usuario
        self._janela = master
        self._janela.title('Gestão Fácil/Extratos')
        self._janela.geometry('850x500')

        # Frame principal para conter tudo
        frame_principal = ttk.Frame(self._janela)
        frame_principal.grid(row=0, column=0, sticky='nsew')
        self._janela.grid_rowconfigure(0, weight=1)
        self._janela.grid_columnconfigure(0, weight=1)

        # Frame para conter o menu e a tabela
        frame_menu_tabela = ttk.Frame(frame_principal)
        frame_menu_tabela.grid(row=1, column=0, sticky='nsew')
        frame_principal.grid_rowconfigure(1, weight=1)
        frame_principal.grid_columnconfigure(0, weight=1)

        # Frame no topo da janela para conter o menu
        frame_menu = ttk.Frame(frame_menu_tabela)
        frame_menu.grid(row=0, column=0, columnspan=2, sticky='ew')
        margin_menu = 3

        # Adicione um novo Frame para "Resumo do mês"
        frame_resumo = ttk.Frame(frame_menu)
        frame_resumo.grid(row=0, column=2, columnspan=5)
        frame_resumo.grid_rowconfigure(0, weight=1)
        frame_resumo.grid_columnconfigure(0, weight=1)

        # Adicione um rótulo para "Resumo do mês" e centralize-o verticalmente com pack
        label_resumo = ttk.Label(frame_resumo, text='Resumo do mês', font=('Helvetica', 16))
        label_resumo.pack(expand=True, pady=10)

        #botões do menu
        self._btn_perfil = ttk.Button(frame_menu, text='Meu perfil', width=20, bootstyle="success", command=self.abrir_perfil)
        self._btn_perfil.grid(row=0, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_inicio = ttk.Button(frame_menu, text='Inicio', width=20, bootstyle="success")
        self._btn_inicio.grid(row=1, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_regis = ttk.Button(frame_menu, text='Registrar Transação', width=20, bootstyle="success", command=self.abrir_transacoes) 
        self._btn_regis.grid(row=2, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_extrato = ttk.Button(frame_menu, text='Extrato', width=20, bootstyle="success")
        self._btn_extrato.grid(row=3, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_contas = ttk.Button(frame_menu, text='Minhas contas', width=20, bootstyle="success")
        self._btn_contas.grid(row=4, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_voltar = ttk.Button(frame_menu, text='Voltar', width=20, bootstyle="success", command=self.voltar) 
        self._btn_voltar.grid(row=5, column=0, sticky='w', pady=margin_menu, padx=margin_menu)


       #tabela
        self._tabela = ttk.Treeview(frame_menu_tabela, columns=('Data', 'Descrição do gasto', 'Categoria', 'Valor do gasto'))

        #scrollbar
        self._scrollbar = ttk.Scrollbar(frame_menu_tabela, orient='vertical', command=self._tabela.yview)
        self._tabela.configure(yscrollcommand=self._scrollbar.set)
        
        # larguras das colunas
        self._tabela.column('#0', width=0)
        self._tabela.column('Data', width=100)
        self._tabela.column('Descrição do gasto', width=100)
        self._tabela.column('Categoria', width=100)
        self._tabela.column('Valor do gasto', width=100)

        #cabeçalhos das colunas
        self._tabela.heading('#0', text='', anchor=W)
        self._tabela.heading('Data', text='Data', anchor=W)
        self._tabela.heading('Descrição do gasto', text='Descrição do gasto', anchor=W)
        self._tabela.heading('Categoria', text='Categoria', anchor=W)
        self._tabela.heading('Valor do gasto', text='Valor do gasto', anchor=W)

           # Posicione a tabela na janela
        self._tabela.grid(row=1, column=0, sticky='nsew')
        self._scrollbar.grid(row=1, column=1, sticky='ns')

        # LabelFrame para "Ganho do mês"
        self._lbl_ganho = ttk.LabelFrame(frame_menu, text='Ganho do mês', bootstyle="success", width=400, height=200)
        self._lbl_ganho.grid(row=2, column=2, padx=10, pady=10, sticky='ew')

        
        # LabelFrame para "Gasto do mês"
        self._lbl_gasto = ttk.LabelFrame(frame_menu, text='Gasto do mês', bootstyle="danger", width=400, height=200)
        self._lbl_gasto.grid(row=2, column=3, padx=10, pady=10, sticky='ew')

        

        # Personalizável, apenas para teste
        ttk.Label(self._lbl_ganho, text='Ganhos do mês vão aqui').pack()
        ttk.Label(self._lbl_gasto, text='Gastos do mês vão aqui').pack()

        # Configurar redimensionamento da tabela
        frame_menu_tabela.grid_rowconfigure(0, weight=0)  # Bloqueia a expansão do menu
        frame_menu_tabela.grid_rowconfigure(1, weight=1)
        frame_menu_tabela.grid_columnconfigure(0, weight=1)
        frame_menu_tabela.grid_columnconfigure(1, weight=0)  # Bloqueia a expansão do scrollbar

        # Configurar redimensionamento do frame_principal
        frame_principal.grid_rowconfigure(0, weight=1)
        frame_principal.grid_columnconfigure(0, weight=1)
        
        
    def abrir_perfil(self):
        perfil_window = PerfilUsuario(self._janela)
    
    def abrir_extratro(self):
        self._janela_Extrato = tk.Toplevel(self._janela)

        extrato_window = Extratos(self._janela_Extrato)
        
    
    def abrir_transacoes(self):
        self._janela_transacoes = tk.Toplevel(self._janela)
        transacao = RegistrarTransacoes(self._janela_transacoes, self._id_usuario_atual)
        
    def voltar(self):
        self._janela.destroy()

if __name__ == "__main__":
    root = ttk.Window(themename='litera')
    login = Extratos(root)
    root.mainloop()