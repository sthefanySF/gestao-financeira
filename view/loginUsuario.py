import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import webbrowser

def open_link(event):
    webbrowser.open("https://www.example.com")  # Substitua pelo link real

janela = ttk.Window(themename='litera')
janela.geometry('700x400')
# GestãoFácil
janela.title('Gestão Fácil/Login')

parte_verde = tk.Label(janela, background='#33bc7d')

image = Image.open(r"C:\Users\Emilly\Desktop\gestao-financeira\logo (4).png")  # Substitua pelo caminho real da imagem
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(parte_verde, image=photo, bg='#33bc7d',width=450)
image_label.pack()

parte_verde.grid(row=0, column=0, rowspan=4, sticky="w")

frame_login = ttk.Frame(janela)
frame_login.grid(row=0, column=1)

lbl_logo = ttk.Label(frame_login, text='Entre ou crie sua conta')
lbl_logo.config(font="Arial 10 bold")
lbl_logo.grid(row=0, column=2, columnspan=4, pady=50)

lbl_email = ttk.Label(frame_login, text='Email:', width=30).grid(row=1, column=3, sticky="e")
etr_email = ttk.Entry(frame_login, width=30).grid(row=2, column=3, sticky="e")

lbl_senha = ttk.Label(frame_login, text='Senha:', width=30).grid(row=3, column=3, sticky="e")
etr_senha = ttk.Entry(frame_login, width=30).grid(row=4, column=3, sticky="e")

link_label = ttk.Label(frame_login, text="esqueci a senha", cursor="hand2", font=("Helvetica", 8, "underline"))
link_label.grid(row=5, column=3, sticky="e")  # Centraliza na coluna da direita
link_label.bind("<Button-1>", open_link)

btn = ttk.Button(frame_login, text='Entrar', width=20,bootstyle="success").grid(row=6, column=3, pady=10)
btn_cadastrar = ttk.Button(frame_login, text='Cadastar',bootstyle="success-outline").grid(row=7, column=3, pady=10)

# Configuração das colunas e linhas do grid
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)
janela.grid_rowconfigure(3, weight=1)

janela.mainloop()
