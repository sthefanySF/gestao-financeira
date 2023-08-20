import sqlite3


class Conexao:
    
    def salvar_no_banco(self,sql):
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()

        cursor.execute(sql)

        # Salvar as mudanças e fechar a conexão
        conexao.commit()
        conexao.close()
    
    @staticmethod
    def retornar_todos(sql):
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()

        # Selecionar todos os usuários da tabela
        cursor.execute(sql)
        usuarios = cursor.fetchall()

        # Fechar a conexão
        conexao.close()
        
        return usuarios
    
    @staticmethod
    def deletar(sql):
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()

        # Deletar um usuário da tabela por ID
        cursor.execute(sql)

        # Salvar as mudanças e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def atualizar(sql):
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()
        cursor.execute(sql)

        conexao.commit()
        conexao.close()
   
    @classmethod
    def autenticar(cls, email, senha):
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()

        # Selecionar usuário pelo email
        cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
        usuario = cursor.fetchone()

        # Fechar a conexão
        conexao.close()

        if usuario and usuario[3] == senha:
            return usuario[0]#retorando o id do usuario encontrado
        else:
            return False