import sqlite3

class Transacao:
    def __init__(self, id_usuario, valor, descricao, categoria, data):
        self.id_usuario = id_usuario
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria
        self.data = data
        self.salvar_no_banco()

    def salvar_no_banco(self):
        # Conectar ao banco de dados
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()

        # Inserir a transação na tabela de transações
        cursor.execute('''
            INSERT INTO transacoes (id_usuario, valor, descricao, categoria, data)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.id_usuario, self.valor, self.descricao, self.categoria, self.data))

        # Salvar as mudanças e fechar a conexão
        conexao.commit()
        conexao.close()

        print("Transação registrada com sucesso!")
