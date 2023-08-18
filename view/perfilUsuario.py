import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk




class PerfilUsuario:
    _photo = None  # Atributo de classe para manter a referência à imagem

    def __init__(self, master):
        self._janela = ttk.Toplevel(master)
        self._janela.title('Gestão Fácil/Meu Perfil')
        self._janela.geometry('800x500')

        # Frame central para posicionar os widgets
        self._frame_central = ttk.Frame(self._janela)
        self._frame_central.pack(expand=True)

        
        self._lbl_nome_usuario = ttk.Label(self._frame_central, text='Nome de Usuário', font='Helvetica 18 bold') #tem que vim o nome de cordo com a conta logada
        self._lbl_nome_usuario.grid(row=0, column=0, columnspan=2, pady=20)
        

        self._btn_meus_dados = ttk.Button(self._frame_central, text='Meus Dados', width=30,  bootstyle="success-outline", command=self.abrir_meus_dados)
        self._btn_meus_dados.grid(row=1, column=0, columnspan=2, pady=10) 

        self._btn_categoria = ttk.Button(self._frame_central, text='Categoria',width=30,  bootstyle="success-outline", command=self.abrir_categoria)
        self._btn_categoria.grid(row=2, column=0, columnspan=2, pady=10)  

        self._btn_seguranca = ttk.Button(self._frame_central, text='Segurança', width=30, bootstyle="success-outline", command=self.abrir_seguranca)
        self._btn_seguranca.grid(row=3, column=0, columnspan=2, pady=10)  

        self._btn_sair = ttk.Button(self._frame_central, text='Sair da Conta', width=30, bootstyle="success-outline", command=self.sair)
        self._btn_sair.grid(row=4, column=0, columnspan=2, pady=10) 

        self._btn_voltar = ttk.Button(self._frame_central, text='Voltar', width=30, bootstyle="success-outline", command=self.voltar)
        self._btn_voltar.grid(row=5, column=0, columnspan=2, pady=10)

        self._janela.mainloop()

    def abrir_meus_dados(self):
        from dadosUsuario import MeusDados

        meus_dados_toplevel = tk.Toplevel(self._janela)
        meus_dados_window = MeusDados(meus_dados_toplevel)

    def abrir_categoria(self):
        pass

    def abrir_seguranca(self):
        pass

   
    def sair(self):
        self._janela.destroy()
        from loginUsuario import Login
        # Recriar a janela de login sem o argumento de tema
        root = ttk.Window()
        login = Login(root)
        root.mainloop()

    def voltar(self):
        pass

if __name__ == "__main__":
    root = ttk.Window(theme='litera') 
    perfil = PerfilUsuario(root)
    root.mainloop()
