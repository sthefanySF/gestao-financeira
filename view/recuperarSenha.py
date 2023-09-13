import sys
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
sys.path.insert(0, './')
sys.path.insert(0, './models')
from models.conexao import Conexao

class RecuperarSenha:
    def __init__(self, master):
        self._janela = master
        self._janela.title('Recuperação de Senha')
        self._janela.geometry('800x500')
        self._id = " "

        self.frame_recuperacao = ttk.Frame(self._janela)
        self.frame_recuperacao.pack(expand=True)

        self._lbl_titulo = ttk.Label(self.frame_recuperacao, text='Recuperação de Senha', font='Helvetica 18 bold')
        self._lbl_titulo.grid(row=0, column=1, columnspan=3, pady=20)

        self.email_label = ttk.Label(self.frame_recuperacao, text="Email:", width=20)
        self.email_label.grid(row=1, column=1, padx=10, pady=5, columnspan=1)
        self.email_entry = ttk.Entry(self.frame_recuperacao, width=50, bootstyle="success-primary")
        self.email_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky="w")

        confirmar_email_botao = ttk.Button(self.frame_recuperacao, text="Confirmar Email", command=self.confirmar_email, width=15, bootstyle="success-outline")
        confirmar_email_botao.grid(row=3, column=1, pady=10, columnspan=4)

        self.nova_senha_entry = None

        # Botão "Voltar"
        voltar_botao = ttk.Button(self.frame_recuperacao, text="Voltar", command=self.voltar, width=15, bootstyle="success-outline")
        voltar_botao.grid(row=4, column=1, pady=10, columnspan=4)

    def confirmar_email(self):
        email = self.email_entry.get()
        resposta = Conexao.retornar_usuario(f"SELECT id FROM usuarios WHERE email = '{email}';")

        if resposta:
            self._id = resposta[0][0]
            print(self._id)
            self.email_entry.grid_remove()
            self._lbl_titulo.config(text='Digite sua nova senha:')
            self.email_label.config(text=' Nova senha:')
            self.nova_senha_entry = ttk.Entry(self.frame_recuperacao, width=50, bootstyle="success-primary")
            self.nova_senha_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky="w")

            # Altere o botão para "Atualizar Senha"
            confirmar_email_botao = ttk.Button(self.frame_recuperacao, text="Atualizar Senha", command=self.atualizar_senha, width=15, bootstyle="success-outline")
            confirmar_email_botao.grid(row=3, column=1, pady=10, columnspan=4)
        else:
            messagebox.showerror('Erro', 'Email não encontrado.')

    def atualizar_senha(self):
        nova_senha = self.nova_senha_entry.get()

        sql = f'''UPDATE usuarios SET senha = '{nova_senha}' WHERE id = {self._id};'''
        Conexao.atualizar(sql)
        messagebox.showinfo('Sucesso', 'Senha atualizada com sucesso!')
        self._janela.destroy()

    def voltar(self):
        self._janela.destroy()  # Fecha a janela atual

if __name__ == "__main__":
    root = tk.Tk()
    recuperar_senha = RecuperarSenha(root)
    root.mainloop()
