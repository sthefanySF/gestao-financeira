import sqlite3

class Usuario:
    def __init__(self, nome, email, senha):
        self._nome = nome
        self._email = email
        self._senha = senha
        self.salvar_no_banco()
    
    def salvar_no_banco(self):
        # Conectar ao banco de dados (ou criar se não existir)
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()

        # Inserir um novo usuário na tabela
        cursor.execute('''
            INSERT INTO usuarios (nome, email, senha)
            VALUES (?, ?, ?)
        ''', (self._nome, self._email, self._senha))

        # Salvar as mudanças e fechar a conexão
        conexao.commit()
        conexao.close()
    
    @staticmethod
    def retornar_todos():
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()

        # Selecionar todos os usuários da tabela
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()

        # Fechar a conexão
        conexao.close()
        
        return usuarios
    
    @staticmethod
    def deletar(id_usuario):
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()

        # Deletar um usuário da tabela por ID
        cursor.execute('DELETE FROM usuarios WHERE id = ?', (id_usuario,))

        # Salvar as mudanças e fechar a conexão
        conexao.commit()
        conexao.close()

    @staticmethod
    def atualizar(id_usuario, nome, email, senha):
        conexao = sqlite3.connect('gestao_financeira.db')
        cursor = conexao.cursor()

        # Atualizar um usuário da tabela por ID
        cursor.execute('''
            UPDATE usuarios
            SET nome = ?, email = ?, senha = ?
            WHERE id = ?
        ''', (nome, email, senha, id_usuario))

        # Salvar as mudanças e fechar a conexão
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
            return usuario[0]
        else:
            return False