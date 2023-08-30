import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import sys


sys.path.insert(0, './')
sys.path.insert(0, './controller')
from controller import usuario
from controller.usuario import Usuario
from perfilUsuario import PerfilUsuario
from registrarTransacao import RegistrarTransacoes

from controller.registrarGanho import RegistrarGanho

class Extratos:
    def __init__(self, master):
        self._id_usuario_atual = usuario
        self._janela = master
        self._janela.title('Gestão Fácil/Extratos')
        self._janela.geometry('1030x800')

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

        # Frame para "Resumo do mês"
        frame_resumo = ttk.Frame(frame_menu)
        frame_resumo.grid(row=0, column=2, columnspan=5)
        frame_resumo.grid_rowconfigure(0, weight=1)
        frame_resumo.grid_columnconfigure(0, weight=1)

        label_resumo = ttk.Label(frame_resumo, text='Resumo do mês', font=('Helvetica', 16))
        label_resumo.pack(expand=True, pady=10)

         #LabelFrame para Ganho do mês
        self._lbl_ganho_mes = ttk.LabelFrame(frame_menu, text='Ganho do mês', bootstyle="success", width=400, height=200)
        self._lbl_ganho_mes.grid(row=1, column=2, padx=10, pady=10, sticky='ew', rowspan=5)

        # LabelFrame para Gasto do mês
        self._lbl_gasto_mes = ttk.LabelFrame(frame_menu, text='Gasto do mês', bootstyle="danger", width=400, height=200)
        self._lbl_gasto_mes.grid(row=1, column=3, padx=10, pady=10, sticky='ew', rowspan=5)


        # Botões do menu
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

        # LabelFrame para Ganhos para a tabela de ganhos
        self._lbl_ganhos = ttk.LabelFrame(frame_menu_tabela, text='Ganhos', bootstyle="success", width=400, height=200)
        self._lbl_ganhos.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        # Tabela de Ganhos
        self._tabela_ganhos = ttk.Treeview(self._lbl_ganhos, columns=('Ganho Mensal', 'Ganho Adicional', 'Descrição do Ganho Adicional'))

        # Larguras das colunas para a tabela de ganhos
        self._tabela_ganhos.column('#0', width=0)
        self._tabela_ganhos.column('Ganho Mensal', width=100)
        self._tabela_ganhos.column('Ganho Adicional', width=100)
        self._tabela_ganhos.column('Descrição do Ganho Adicional', width=200)

        # Cabeçalhos das colunas para a tabela de ganhos
        self._tabela_ganhos.heading('#0', text='', anchor=W)
        self._tabela_ganhos.heading('Ganho Mensal', text='Ganho Mensal', anchor=W)
        self._tabela_ganhos.heading('Ganho Adicional', text='Ganho Adicional', anchor=W)
        self._tabela_ganhos.heading('Descrição do Ganho Adicional', text='Descrição do Ganho Adicional', anchor=W)


        # Scrollbar para a tabela de ganhos
        self._scrollbar_ganhos = ttk.Scrollbar(self._lbl_ganhos, orient='vertical', command=self._tabela_ganhos.yview)
        self._tabela_ganhos.configure(yscrollcommand=self._scrollbar_ganhos.set)


        self._tabela_ganhos.grid(row=0, column=0, sticky='nsew')
        self._scrollbar_ganhos.grid(row=0, column=1, sticky='ns')

        
        self._lbl_ganhos.grid_rowconfigure(0, weight=1)
        self._lbl_ganhos.grid_columnconfigure(0, weight=1)
        self.atualizar_tabela_ganhos()  # Chame este método para carregar os ganhos na inicialização

        #LabelFrame para Gastos
        self._lbl_gastos = ttk.LabelFrame(frame_menu_tabela, text='Gastos', bootstyle="danger", width=400, height=200)
        self._lbl_gastos.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

        # Tabela de Gastos
        self._tabela_gastos = ttk.Treeview(self._lbl_gastos, columns=('Data', 'Descrição do gasto', 'Categoria', 'Valor do gasto'))

        
        self._tabela_gastos.column('#0', width=0)
        self._tabela_gastos.column('Data', width=100)
        self._tabela_gastos.column('Descrição do gasto', width=100)
        self._tabela_gastos.column('Categoria', width=100)
        self._tabela_gastos.column('Valor do gasto', width=100)

      
        self._tabela_gastos.heading('#0', text='', anchor=W)
        self._tabela_gastos.heading('Data', text='Data', anchor=W)
        self._tabela_gastos.heading('Descrição do gasto', text='Descrição do gasto', anchor=W)
        self._tabela_gastos.heading('Categoria', text='Categoria', anchor=W)
        self._tabela_gastos.heading('Valor do gasto', text='Valor do gasto', anchor=W)

        # Scrollbar para a tabela de gastos
        self._scrollbar_gastos = ttk.Scrollbar(self._lbl_gastos, orient='vertical', command=self._tabela_gastos.yview)
        self._tabela_gastos.configure(yscrollcommand=self._scrollbar_gastos.set)

        
        self._tabela_gastos.grid(row=0, column=0, sticky='nsew')
        self._scrollbar_gastos.grid(row=0, column=1, sticky='ns')

       
        self._lbl_gastos.grid_rowconfigure(0, weight=1)
        self._lbl_gastos.grid_columnconfigure(0, weight=1)

    
        frame_menu_tabela.grid_rowconfigure(0, weight=1)
        frame_menu_tabela.grid_columnconfigure(0, weight=1)

    def abrir_perfil(self):
        perfil_window = PerfilUsuario(self._janela)
    
    def abrir_transacoes(self):
        self._janela_transacoes = tk.Toplevel(self._janela)
        transacao = RegistrarTransacoes(self._janela_transacoes, self._id_usuario_atual)
        
    def voltar(self):
        self._janela.destroy()

    def registar_ganho(self):
        ganho_mensal = self._entry_ganho_mensal.get()
        ganho_adicional = self._entry_ganho_adicional.get()
        descricao = self._text_descricao_ganhos.get('1.0', 'end')
      
        novo_ganho = RegistrarGanho(self._id_usuario_atual, ganho_mensal, ganho_adicional, descricao)
        
        # Após inserir um novo ganho, atualize a tabela de ganhos
        self.atualizar_tabela_ganhos()
        
        return messagebox.showinfo("Registro de ganho", "Ganho registrado com sucesso!")

    def atualizar_tabela_ganhos(self):
        # Limpe os itens existentes na tabela
        for item in self._tabela_ganhos.get_children():
            self._tabela_ganhos.delete(item)
        
        # Obtenha todos os ganhos do banco de dados
        ganhos = RegistrarGanho.retornar_todos()
        
        # Insira os ganhos na tabela
        for ganho in ganhos:
            self._tabela_ganhos.insert('', 'end', values=ganho[2:])  # Ignora o primeiro valor (ID)

if __name__ == "__main__":
    root = ttk.Window(themename='litera')
    login = Extratos(root)
    root.mainloop()
