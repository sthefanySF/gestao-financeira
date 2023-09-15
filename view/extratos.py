import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import sys

from controller.reegistrarGasto import RegistrarGasto
from view.editarGanho import JanelaEdicaoGanho
from view.editarGasto import JanelaEdicaoGasto




sys.path.insert(0, './')
sys.path.insert(0, './controller')
from controller import usuario
from controller.usuario import Usuario
from perfilUsuario import PerfilUsuario
from registrarTransacao import RegistrarTransacoes
from controller.registrarGanho import RegistrarGanho

class Extratos:
    def __init__(self, master, usuario):
        self._id_usuario_atual = usuario
        self._janela = master
        self._janela.title('Gestão Fácil/Extratos')
        self._janela.geometry('1000x900')

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

        # LabelFrame para Ganho do mês
        self._lbl_ganho_mes = ttk.LabelFrame(frame_menu, text='Ganho do mês', bootstyle="success")
        self._lbl_ganho_mes.grid(row=1, column=2, padx=10, pady=10, sticky='ew', rowspan=5)
    
        self.lbl_ganho = ttk.Label(self._lbl_ganho_mes, text=self.ganhos_totais())
        self.lbl_ganho.config(font="Arial 30 bold")
        self.lbl_ganho.pack()

        # LabelFrame para Gasto do mês
        self._lbl_gasto_mes = ttk.LabelFrame(frame_menu, text='Gasto do mês', bootstyle="danger")
        self._lbl_gasto_mes.grid(row=1, column=3, padx=10, pady=10, sticky='ew', rowspan=5)

        self.lbl = ttk.Label(self._lbl_gasto_mes, text=self.gastos_totais())
        self.lbl.config(font="Arial 30 bold")
        self.lbl.pack()

        # Botões do menu        
        self._btn_perfil = ttk.Button(frame_menu, text='Meu perfil', width=20, bootstyle="success", command=self.abrir_perfil)
        self._btn_perfil.grid(row=0, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_inicio = ttk.Button(frame_menu, text='Inicio', width=20, bootstyle="success", command=self.entrar)
        self._btn_inicio.grid(row=1, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_regis = ttk.Button(frame_menu, text='Registrar Transação', width=20, bootstyle="success", command=self.abrir_transacoes) 
        self._btn_regis.grid(row=2, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        self._btn_extrato = ttk.Button(frame_menu, text='Extrato', width=20, bootstyle="success")
        self._btn_extrato.grid(row=3, column=0, sticky='w', pady=margin_menu, padx=margin_menu)

        
        # LabelFrame para Ganhos para a tabela de ganhos
        self._lbl_ganhos = ttk.LabelFrame(frame_menu_tabela, text='Ganhos', bootstyle="success")
        self._lbl_ganhos.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
         #LabelFrame para Gastos
        self._lbl_gastos = ttk.LabelFrame(frame_menu_tabela, text='Gastos', bootstyle="danger", width=400, height=400)
        self._lbl_gastos.grid(row=2, column=0, padx=10, pady=10, sticky='nsew') 

        # Frame para botões de "Editar Ganho" e "Excluir Ganho"
        frame_botoes_ganho = ttk.Frame(self._lbl_ganhos)
        frame_botoes_ganho.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        # Frame para botões de "Editar Gasto" e "Excluir Gasto"
        frame_botoes_gasto = ttk.Frame(self._lbl_gastos)
        frame_botoes_gasto.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
                
        # Criar botões para editar e excluir ganhos
        self._btn_editar_ganho = ttk.Button(frame_botoes_ganho, text='Editar Ganho', bootstyle="success-outline", command=self.editar_ganho)
        self._btn_excluir_ganho = ttk.Button(frame_botoes_ganho, text='Excluir Ganho', bootstyle="success-outline", command=self.excluir_ganho)

        # Criar botões para editar e excluir gastos
        self._btn_editar_gasto = ttk.Button(frame_botoes_gasto, text='Editar Gasto', bootstyle="success-outline", command=self.editar_gasto)
        self._btn_excluir_gasto = ttk.Button(frame_botoes_gasto, text='Excluir Gasto', bootstyle="success-outline", command=self.excluir_gasto)

        # Posicionamento dos botões "Editar" e "Excluir" para ganhos e gastos usando grid
        self._btn_editar_ganho.grid(row=3, column=1, padx=(20, 10), pady=10, sticky='e')
        self._btn_excluir_ganho.grid(row=3, column=2, padx=(20, 20), pady=10, sticky='w')
        
        
        self._btn_editar_gasto.grid(row=0, column=0, padx=10, pady=10)  # Defina a linha e a coluna conforme necessário
        self._btn_excluir_gasto.grid(row=0, column=1, padx=10, pady=10)  # Defina a linha e a coluna conforme necessário


        

        # Tabela de Ganhos
        self._tabela_ganhos = ttk.Treeview(self._lbl_ganhos, columns=('Ganho Mensal', 'Ganho Adicional', 'Descrição do Ganho Adicional', 'Data'))

        # Larguras das colunas para a tabela de ganhos
        self._tabela_ganhos.column('#0', width=0)
        self._tabela_ganhos.column('Ganho Mensal', width=100)
        self._tabela_ganhos.column('Ganho Adicional', width=100)
        self._tabela_ganhos.column('Descrição do Ganho Adicional', width=100)
        self._tabela_ganhos.column('Data', width=100)

        # Cabeçalhos das colunas para a tabela de ganhos
        self._tabela_ganhos.heading('#0', text='', anchor=W)
        self._tabela_ganhos.heading('Ganho Mensal', text='Ganho Mensal', anchor=W)
        self._tabela_ganhos.heading('Ganho Adicional', text='Ganho Adicional', anchor=W)
        self._tabela_ganhos.heading('Descrição do Ganho Adicional', text='Descrição do Ganho Adicional', anchor=W)
        self._tabela_ganhos.heading('Data', text='Data', anchor=W)


        # Scrollbar para a tabela de ganhos
        self._scrollbar_ganhos = ttk.Scrollbar(self._lbl_ganhos, orient='vertical', command=self._tabela_ganhos.yview)
        self._tabela_ganhos.configure(yscrollcommand=self._scrollbar_ganhos.set)


        self._tabela_ganhos.grid(row=0, column=0, sticky='nsew')
        self._scrollbar_ganhos.grid(row=0, column=1, sticky='ns')

        
        self._lbl_ganhos.grid_rowconfigure(0, weight=1)
        self._lbl_ganhos.grid_columnconfigure(0, weight=1)
        self.atualizar_tabela_ganhos()  # Chame este método para carregar os ganhos na inicialização


        # Tabela de Gastos
        self._tabela_gastos = ttk.Treeview(self._lbl_gastos, columns=('Valor do gasto', 'Descrição do gasto', 'Categoria', 'Data'))

        
        self._tabela_gastos.column('#0', width=0)
        self._tabela_gastos.column('Valor do gasto', width=100)
        self._tabela_gastos.column('Descrição do gasto', width=100)
        self._tabela_gastos.column('Categoria', width=100)
        self._tabela_gastos.column('Data', width=100)

      
        self._tabela_gastos.heading('#0', text='', anchor=W)
        self._tabela_gastos.heading('Valor do gasto', text='Valor do gasto', anchor=W)
        self._tabela_gastos.heading('Descrição do gasto', text='Descrição do gasto', anchor=W)
        self._tabela_gastos.heading('Categoria', text='Categoria', anchor=W)
        self._tabela_gastos.heading('Data', text='Data', anchor=W)

        # Scrollbar para a tabela de gastos
        self._scrollbar_gastos = ttk.Scrollbar(self._lbl_gastos, orient='vertical', command=self._tabela_gastos.yview)
        self._tabela_gastos.configure(yscrollcommand=self._scrollbar_gastos.set)

        
        self._tabela_gastos.grid(row=0, column=0, sticky='nsew')
        self._scrollbar_gastos.grid(row=0, column=1, sticky='ns')

       
        self._lbl_gastos.grid_rowconfigure(0, weight=1)
        self._lbl_gastos.grid_columnconfigure(0, weight=1)

        self.atualizar_tabela_gastos() 
        frame_menu_tabela.grid_rowconfigure(0, weight=1)
        frame_menu_tabela.grid_columnconfigure(0, weight=1)
        self.atualizar_tabela_gastos()

    def abrir_perfil(self):
        #self._janela.withdraw()
        perfil_window = PerfilUsuario(self._janela,self._id_usuario_atual)
    
    def abrir_transacoes(self):
        self._janela.withdraw()
        self._janela_transacoes = tk.Toplevel(self._janela)
        transacao = RegistrarTransacoes(self._janela_transacoes, self._id_usuario_atual)
        
    def entrar(self):
        self._janela.withdraw()
        from telaInicial import TelaInicial
        tela_inicial_toplevel = tk.Toplevel(self._janela)
        tela_inicial = TelaInicial(tela_inicial_toplevel, self._id_usuario_atual)
        
        
    def voltar(self):
        self._janela.destroy()

    def registar_ganho(self):
        ganho_mensal = self._entry_ganho_mensal.get()
        ganho_adicional = self._entry_ganho_adicional.get()
        descricao = self._text_descricao_ganhos.get('1.0', 'end')
      
        novo_ganho = RegistrarGanho(self._id_usuario_atual, ganho_mensal, ganho_adicional, descricao)
        
        self.atualizar_tabela_ganhos()
        
        return messagebox.showinfo("Registro de ganho", "Ganho registrado com sucesso!")

    def atualizar_tabela_ganhos(self):
        for item in self._tabela_ganhos.get_children():
            self._tabela_ganhos.delete(item)
        
        ganhos = RegistrarGanho.retornar_unico_usuario(self._id_usuario_atual)
        
        for ganho in ganhos:
            self._tabela_ganhos.insert('', 'end', values=ganho[2:])  # Ignora o primeiro valor (ID)
        
    def atualizar_tabela_gastos(self):
        for item in self._tabela_gastos.get_children():
            self._tabela_gastos.delete(item)

        gastos = RegistrarGasto.retornar_gastos(self._id_usuario_atual)
        for gasto in gastos:
            self._tabela_gastos.insert('', 'end', values=gasto[2:])

    def gastos_totais(self):
        valor = RegistrarGasto.retornar_total_gastos(self._id_usuario_atual)
        for i in valor:
            valor = str(i[0])
        return valor
    
    def ganhos_totais(self):
        valor = RegistrarGanho.ganho_total(self._id_usuario_atual)
        for i in valor:
            valor = str(i[0])
        return valor
    
    
    def editar_ganho(self):
        selected_item = self._tabela_ganhos.selection()

        if not selected_item:
            messagebox.showerror("Erro na edição de ganho", "Selecione um ganho para editar.")
            return

        item_id = selected_item[0]
        ganho_values = self._tabela_ganhos.item(item_id, 'values')
        ganho_mensal = ganho_values[0]
        ganho_adicional = ganho_values[1]
        descricao = ganho_values[2]

        
        edicao_ganho = JanelaEdicaoGanho(self._janela, item_id, ganho_mensal, ganho_adicional, descricao, self.salvar_edicao_ganho)


    def editar_gasto(self):
        selected_item = self._tabela_gastos.selection()

        if not selected_item:
            messagebox.showerror("Erro na edição de gasto", "Selecione um gasto para editar.")
            return

        item_id = selected_item[0]
        gasto_values = self._tabela_gastos.item(item_id, 'values')
        valor_gasto = gasto_values[0]
        descricao_gasto = gasto_values[1]
        categoria_gasto = gasto_values[2]
        data_gasto = gasto_values[3]

        edicao_gasto = JanelaEdicaoGasto(self._id_usuario_atual,self._janela, item_id, valor_gasto, descricao_gasto, categoria_gasto, data_gasto, self.salvar_edicao_gasto)


    def salvar_edicao_ganho(self, item_id, novo_ganho_mensal, novo_ganho_adicional, nova_descricao):
        self._tabela_ganhos.item(item_id, values=(novo_ganho_mensal, novo_ganho_adicional, nova_descricao))

        messagebox.showinfo("Edição de ganho", "Ganho editado com sucesso.")

    
    def salvar_edicao_gasto(self, item_id, novo_valor, nova_descricao, nova_categoria, nova_data):
        self._tabela_gastos.item(item_id, values=(novo_valor, nova_descricao, nova_categoria, nova_data))

        messagebox.showinfo("Edição de gasto", "Gasto editado com sucesso.")

    
    def excluir_ganho(self):
        selected_ganho = self._tabela_ganhos.selection()

        if not selected_ganho:
            messagebox.showerror('Erro na exclusão', 'Selecione um ganho para excluir.')
            return

        confirmacao = messagebox.askyesno('Confirmação', 'Tem certeza que deseja excluir este ganho?')

        if confirmacao:
            for item in selected_ganho:
                self._tabela_ganhos.delete(item)

    def excluir_gasto(self):
        selected_gasto = self._tabela_gastos.selection()

        if not selected_gasto:
            messagebox.showerror('Erro na exclusão', 'Selecione um gasto para excluir.')
            return

        confirmacao = messagebox.askyesno('Confirmação', 'Tem certeza que deseja excluir este gasto?')

        if confirmacao:
            for item in selected_gasto:
                self._tabela_gastos.delete(item)
                    
                    


        
if __name__ == "__main__":
    root = ttk.Window(themename='litera')
    login = Extratos(root)
    root.mainloop()
