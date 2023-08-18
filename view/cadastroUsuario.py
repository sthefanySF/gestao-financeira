import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import webbrowser





class Cadastro:

    def cadastrar(self):
        from loginUsuario import Login
        Login()
        Cadastro()
        
    def voltar(self):
        from loginUsuario import Login
        self._janela.destroy()
        login_window = ttk.Window(theme='litera')  # Cria uma nova janela de login
        login = Login(login_window)
        login_window.mainloop()
        
        
        

    
        #self._janela = ttk.Toplevel(themename='litera')
    def __init__(self, master, photo):
        self._janela = master
        self._janela.title('Gestão Fácil/Cadastro')
        self._janela.geometry('800x500')
        self._photo = photo  


        self._parte_verde = tk.Label(self._janela, background='#33bc7d')

        image = Image.open(r"C:\Users\sthef\OneDrive\Documentos\GitHub\gestao-financeira\logo (4).png")
        photo = ImageTk.PhotoImage(image)
        self._image_label = tk.Label(self._parte_verde, image=photo, bg='#33bc7d', width=450)
        self._image_label.image = photo  # Mantenha a referência à imagem
        self._image_label.pack()

        self._parte_verde.grid(row=0, column=0, rowspan=4, sticky="w")

        self._frame_cadastro = ttk.Frame(self._janela)
        self._frame_cadastro.grid(row=0, column=1)

        self._lbl_nome = ttk.Label(self._frame_cadastro, text='Nome:', width=30).grid(row=1, column=3, sticky="e")
        self._etr_nome = ttk.Entry(self._frame_cadastro, width=30).grid(row=2, column=3, sticky="e")

        self._lbl_email = ttk.Label(self._frame_cadastro, text='Email:', width=30).grid(row=3, column=3, sticky="e")
        self._etr_email = ttk.Entry(self._frame_cadastro, width=30).grid(row=4, column=3, sticky="e")

        self._lbl_senha = ttk.Label(self._frame_cadastro, text='Senha:', width=30).grid(row=5, column=3, sticky="e")
        self._etr_senha = ttk.Entry(self._frame_cadastro, width=30).grid(row=6, column=3, sticky="e")

        self._btn_cadastrar = ttk.Button(self._frame_cadastro, text='Cadastrar', width=20, bootstyle="success-outline")
        self._btn_cadastrar.grid(row=7, column=3, pady=10)

        self._btn_voltar = ttk.Button(self._frame_cadastro, text='Voltar', width=15, bootstyle="success-outline", command=self.voltar)
        self._btn_voltar.grid(row=8, column=3, pady=10)
        
        # Configuração das colunas e linhas do grid
        self._janela.grid_columnconfigure(0, weight=1)
        self._janela.grid_columnconfigure(1, weight=1)
        self._janela.grid_rowconfigure(0, weight=1)
        self._janela.grid_rowconfigure(1, weight=1)
        self._janela.grid_rowconfigure(2, weight=1)
        self._janela.grid_rowconfigure(3, weight=1)

        self._janela.mainloop()

