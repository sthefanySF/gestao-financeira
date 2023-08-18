import tkinter as tk
import ttkbootstrap as ttk

class MeusDados:
    def __init__(self, master):
        self._janela = master
        self._janela.title('Gestão Fácil/Dados do Usuário')
        self._janela.geometry('800x500')

        self.frame_dados = ttk.Frame(self._janela)
        self.frame_dados.pack(expand=True)
        
        self._lbl_nome_usuario = ttk.Label(self.frame_dados, text='Meus Dados', font='Helvetica 18 bold')
        self._lbl_nome_usuario.grid(row=0, column=0, columnspan=2, pady=20)

        nome_label = ttk.Label(self.frame_dados, text="Nome:", width=20)
        nome_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.nome_entry = ttk.Entry(self.frame_dados, width=50, bootstyle="success-primary")
        self.nome_entry.grid(row=2, column=1, padx=10, pady=5)

        email_label = ttk.Label(self.frame_dados, text="E-mail:", width=20)
        email_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.email_entry = ttk.Entry(self.frame_dados, width=50, bootstyle="success-primary")
        self.email_entry.grid(row=4, column=1, padx=10, pady=5)
        atualizar_botao = ttk.Button(self.frame_dados, text="Atualizar Informações", command=self.atualizar_informacoes, width=20, bootstyle="success-primary")

        atualizar_botao.grid(row=5, columnspan=2, pady=10)

    def atualizar_informacoes(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()

        if nome and email:
            # Implemente aqui a lógica para atualizar as informações no banco de dados, por exemplo
            print("Informações atualizadas:")
            print("Nome:", nome)
            print("E-mail:", email)
        else:
            print("Por favor, preencha o nome e o e-mail antes de atualizar.")


if __name__ == "__main__":
    root = ttk.Window()
    app = MeusDados(root)
    root.mainloop()
