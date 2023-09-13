import sqlite3
import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
import sys


sys.path.insert(0, './')
sys.path.insert(0, './controller')
sys.path.insert(0, './models')
from controller import usuario
from conexao import Conexao


class PerfilUsuario:
    _photo = None  # Atributo de classe para manter a referência à imagem

    def __init__(self, master, id_usuario_logado,login_window= None):
        self._janela = ttk.Toplevel(master)
        self._janela.title('Gestão Fácil/Meu Perfil')
        self._janela.geometry('800x500')
        self._login_window = login_window  # Mantenha a referência à janela de login
        nome_usuario = self.obter_nome_usuario_logado(id_usuario_logado)
        self._id_usuario_logado = id_usuario_logado
        

        # Frame central para posicionar os widgets
        self._frame_central = ttk.Frame(self._janela)
        self._frame_central.pack(expand=True)

        
        self._lbl_nome_usuario = ttk.Label(self._frame_central, text=f'{nome_usuario}', font='Helvetica 18 bold')
        self._lbl_nome_usuario.grid(row=0, column=0, columnspan=2, pady=20)
        

        self._btn_meus_dados = ttk.Button(self._frame_central, text='Meus Dados', width=30,  bootstyle="success-outline", command=lambda: self.abrir_meus_dados(id_usuario_logado))
        self._btn_meus_dados.grid(row=1, column=0, columnspan=2, pady=10) 

        self._btn_categoria = ttk.Button(self._frame_central, text='Categoria',width=30,  bootstyle="success-outline", command=self.abrir_categoria)
        self._btn_categoria.grid(row=2, column=0, columnspan=2, pady=10)  

        self._btn_seguranca = ttk.Button(self._frame_central, text='Segurança', width=30, bootstyle="success-outline", command=self.abrir_seguranca)
        self._btn_seguranca.grid(row=3, column=0, columnspan=2, pady=10)  

        self._btn_sair = ttk.Button(self._frame_central, text='Sair da Conta', width=30, bootstyle="success-outline", command=self.sair)
        self._btn_sair.grid(row=4, column=0, columnspan=2, pady=10) 
        
        self._btn_excluir = ttk.Button(self._frame_central, text='Excluir minha conta', width=30, bootstyle="success-outline", command=lambda: self.excluir_conta(id_usuario_logado))
        self._btn_excluir.grid(row=5, column=0, columnspan=2, pady=10)

        self._btn_voltar = ttk.Button(self._frame_central, text='Voltar', width=30, bootstyle="success-outline", command=self.voltar)
        self._btn_voltar.grid(row=6, column=0, columnspan=2, pady=10)

        self._janela.mainloop()

    def abrir_meus_dados(self, id_usuario_logado):
        from dadosUsuario import MeusDados

        # Crie uma instância de Usuario com base no id_usuario_logado
        usuario_logado = usuario.Usuario.obter_usuario_por_id(id_usuario_logado)

        meus_dados_toplevel = tk.Toplevel(self._janela)
        meus_dados_window = MeusDados(meus_dados_toplevel, usuario_logado,self._id_usuario_logado)

    
    def abrir_categoria(self):
        from categorias import Categorias
        Categorias_toplevel = tk.Toplevel(self._janela)
        categorias_window = Categorias(Categorias_toplevel)

    def abrir_seguranca(self):
        from senhaUsuario import SenhaUsuario
        recuperar = tk.Toplevel(self._janela)
        janela = SenhaUsuario(recuperar,self._id_usuario_logado)

   
    def sair(self):
        self._janela.destroy()
        self._login_window.mostrar_login()  # Mostrar a janela de login novamente ao sair
    
    def voltar(self):
        self._janela.destroy()
        
    def obter_nome_usuario_logado(self, id_usuario_logado):
        # Conecte-se ao banco de dados e execute a consulta
        sql = "SELECT nome FROM usuarios WHERE id = ?"
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()
        cursor.execute(sql, (id_usuario_logado,))
        
        # Obtenha o nome do usuário logado
        nome_usuario = cursor.fetchone()[0]  # Assumindo que a primeira coluna é o nome

        # Feche a conexão com o banco de dados
        conexao.close()
    
        return nome_usuario
    
    def excluir_conta(self, id_usuario_logado=None):
        # Abra a conexão com o banco de dados
        print(id_usuario_logado)
        conexao =  Conexao
        sql = f"DELETE FROM usuarios WHERE id = '{id_usuario_logado}';"
        print(sql)
        conexao = Conexao.deletar(sql)
        self._janela.destroy()

        self._login_window.mostrar_login()  # Mostrar a janela de login novamente ao sair


