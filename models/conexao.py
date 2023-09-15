import sqlite3


class Conexao:
    
    @classmethod
    def salvar_no_banco(cls,sql):
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
    def retornar_usuario(sql):
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()

        cursor.execute(sql)
        usuarios = cursor.fetchall()

        conexao.close()

        return usuarios
    

    @staticmethod
    def retornar_um(sql, parametros):
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()

        cursor.execute(sql, parametros)
        resultado = cursor.fetchone()

        conexao.close()

        return resultado
    
    
    
    @staticmethod
    def deletar(sql):
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()

        # Deletar um usuário da tabela por ID
        cursor.execute(sql)

        # Salvar as mudanças e fechar a conexão
        conexao.commit()
        conexao.close()

    @classmethod
    def atualizar(cls,sql):
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
        
Conexao.deletar("DELETE FROM ganhos WHERE id_usuario = 42;")
