import tkinter as tk
import ttkbootstrap as ttk

from conexao import Conexao

class Categorias:
    def __init__(self, master):
        self._janela = master
        self._janela.title('Gestão Fácil/Categorias')
        self._janela.geometry('800x500')

        self.content_frame = ttk.Frame(self._janela)
        self.content_frame.pack(expand=True, fill="both", side="top")

        self.table_frame = ttk.Frame(self.content_frame)
        self.table_frame.pack(side="top", fill="both", expand=True)

        self.table = ttk.Treeview(self.table_frame, columns=("ID", "Nome"))
        self.table.heading("ID", text="ID", anchor="w")
        self.table.heading("Nome", text="Nome", anchor="w")
        self.table.column("#0", width=0, stretch="no")
        self.table.column("ID", width=50)  # Reduzindo a largura da coluna ID
        self.table.column("Nome", minwidth=300, width=300)
        self.table.pack(side="left", fill="both", expand=True)

        self.scroll = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.scroll.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=self.scroll.set)

        self.frame_botoes = ttk.Frame(self.content_frame)
        self.frame_botoes.pack(side="bottom", pady=10)

        self.criar_nova_categoria_botao = ttk.Button(self.frame_botoes, text="Criar nova categoria", width=30, bootstyle="success", command=self.criar_nova_categoria)
        self.criar_nova_categoria_botao.pack(side="left", padx=5)

        self.voltar_botao = ttk.Button(self.frame_botoes, text="Voltar", width=30, bootstyle="success", command=self._janela.destroy)
        self.voltar_botao.pack(side="left", padx=5)

        self.adicionar_categorias_iniciais()

        # Estilização das colunas em negrito
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

    def criar_nova_categoria(self):
        pass

    def adicionar_categorias_iniciais(self): #só para testar a visualização
        categorias = Conexao.retornar_todos('SELECT * FROM categoria;')

        for categoria in categorias:
            self.table.insert("", "end", values=categoria)

if __name__ == "__main__":
    root = ttk.Window(theme="litera")  # Escolha um tema do ttkbootstrap
    app = Categorias(root)
    root.mainloop()
