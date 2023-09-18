import tkinter
from tkinter import ttk
from conexao import Conexao

from controller.reegistrarGasto import RegistrarGasto


class JanelaEdicaoGasto:
    def __init__(self,usuario, master, item_id, valor_gasto, descricao_gasto, categoria_gasto, data_gasto, callback):
        self._master = master
        self._id_usuario = usuario
        self._item_id = item_id
        self._valor_gasto = valor_gasto
        self._descricao_gasto = descricao_gasto
        self._categoria_gasto = categoria_gasto
        self._data_gasto = data_gasto
        self._callback = callback

        self._janela_edicao = tkinter.Toplevel(master)
        self._janela_edicao.title('Editar Gasto')
        self._janela_edicao.geometry('400x300')

        # Campo de edição para o valor do gasto
        label_valor = ttk.Label(self._janela_edicao, text='Valor do Gasto:')
        label_valor.pack()

        self._entry_valor = ttk.Entry(self._janela_edicao)
        self._entry_valor.insert(0, self._valor_gasto)  # Preencha o valor atual
        self._entry_valor.pack()

        # Campo de edição para a descrição do gasto
        label_descricao = ttk.Label(self._janela_edicao, text='Descrição do Gasto:')
        label_descricao.pack()

        self._entry_descricao = ttk.Entry(self._janela_edicao)
        self._entry_descricao.insert(0, self._descricao_gasto)  # Preencha a descrição atual
        self._entry_descricao.pack()

        # Campo de edição para a categoria do gasto
        label_categoria = ttk.Label(self._janela_edicao, text='Categoria do Gasto:')
        label_categoria.pack()

        # self._entry_categoria = ttk.Entry(self._janela_edicao)
        # self._entry_categoria.insert(0, self._categoria_gasto)  # Preencha a categoria atual
        # self._entry_categoria.pack()
        
        ttk.Label(self._janela_edicao, text="Categoria:").pack()
        self._combo_categoria = ttk.Combobox(self._janela_edicao, values= self.categorias())
        self._combo_categoria.pack()
        self._combo_categoria.set(self._categoria_gasto)

        # Campo de edição para a data do gasto
        label_data = ttk.Label(self._janela_edicao, text='Data do Gasto:')
        label_data.pack()

        self._entry_data = ttk.Entry(self._janela_edicao)
        self._entry_data.insert(0, self._data_gasto)  # Preencha a data atual
        self._entry_data.pack()

        # Botão para salvar as alterações
        btn_salvar = ttk.Button(self._janela_edicao, text='Salvar',  bootstyle="success-outline", command=self.salvar_edicao)
        btn_salvar.pack()
    def categorias(self):
        categorias = Conexao.retornar_todos('SELECT nome FROM categoria;')
        return categorias

    def salvar_edicao(self):
        # Obtenha os novos valores dos campos de edição
        novo_valor = self._entry_valor.get()
        nova_descricao = self._entry_descricao.get()
        nova_categoria = self._combo_categoria.get()
        nova_data = self._entry_data.get()
        print(self._id_usuario)
        
        gasto = RegistrarGasto.atualizar(self._id_usuario,novo_valor,nova_descricao,nova_categoria,nova_data)

        # Chame a função de retorno (callback) passando os novos valores
        self._callback(self._item_id, novo_valor, nova_descricao, nova_categoria, nova_data)

        # Feche a janela de edição
        self._janela_edicao.destroy()
